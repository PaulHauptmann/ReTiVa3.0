/*F******************************************************************************
 *
 * openSMILE - open Speech and Music Interpretation by Large-space Extraction
 *       the open-source Munich Audio Feature Extraction Toolkit
 * Copyright (C) 2008-2009  Florian Eyben, Martin Woellmer, Bjoern Schuller
 *
 *
 * Institute for Human-Machine Communication
 * Technische Universitaet Muenchen (TUM)
 * D-80333 Munich, Germany
 *
 *
 * If you use openSMILE or any code from openSMILE in your research work,
 * you are kindly asked to acknowledge the use of openSMILE in your publications.
 * See the file CITING.txt for details.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 ******************************************************************************E*/


/*  openSMILE component: dataWriter */


#include <dataWriter.hpp>

#define MODULE "cDataWriter"


SMILECOMPONENT_STATICS(cDataWriter)

SMILECOMPONENT_REGCOMP(cDataWriter)
{
  SMILECOMPONENT_REGCOMP_INIT
  scname = COMPONENT_NAME_CDATAWRITER;
  sdescription = COMPONENT_DESCRIPTION_CDATAWRITER;

  // configure your component's configType:
  SMILECOMPONENT_CREATE_CONFIGTYPE

  ct->setField("dmInstance", "dataMemory instance to connect to", "dataMemory");
  ct->makeMandatory(ct->setField("dmLevel", "dataMemory level to write to", (char *)NULL));

  if (ct->setField("levelconf", "optional configuration of data memory level\n   (if given, it will overwrite any defaults)",
                  sconfman->getTypeObj("cDataMemory.level"), NO_ARRAY, DONT_FREE) == -1) {
     rA=1; // if subtype not yet found, request , re-register in the next iteration
  }

  SMILECOMPONENT_IFNOTREGAGAIN( {} )

  SMILECOMPONENT_MAKEINFO_NODMEM(cDataWriter);
}

SMILECOMPONENT_CREATE(cDataWriter)

///------------------------------------ dynamic part:

cDataWriter::cDataWriter(const char *_name) : cSmileComponent(_name),
  dm(NULL),
  dmInstName(NULL),
  dmLevel(NULL),
  level(-1),
  override_nT(0)
//  blocksize(1)
{
 // if (cm!=NULL) fetchConfig();
}

void cDataWriter::fetchConfig() {
  // get name of dataMemory instance to connect to
  dmInstName = getStr("dmInstance");
  if (dmInstName == NULL) COMP_ERR("fetchConfig: getStr(dmInstance) returned NULL! missing option in config file?");

  // now get read level information:
  dmLevel = getStr("dmLevel");
  if (dmLevel == NULL) COMP_ERR("fetchConfig: getStr(dmLevel) returned NULL! missing option in config file?");
}

//----- BEGIN obsolete methods --------
// manual configuration:
/*
void cDataWriter::setConfig(int isRb, long nT, double period, double lenSec, int dyn, int _type, int _override)
{
  cfg.isRb = isRb;
  if (!override_nT) cfg.nT = nT;
  cfg.T = period;
  if ((lenSec == 0.0)&&(nT>0)) lenSec = ((double)nT) * period;
  cfg.lenSec = lenSec;
  cfg.frameSizeSec = period;
  cfg.growDyn = dyn;
  cfg.type = _type;
  //override = _override;
  manualConfig = 1;
}

// manual configuration:
void cDataWriter::setConfig(int isRb, long nT, double period, double lenSec, double frameSizeSec, int dyn, int _type, int _override)
{
  cfg.isRb = isRb;
  if (!override_nT) cfg.nT = nT;
  cfg.T = period;
  if ((lenSec == 0.0)&&(nT>0)) lenSec = ((double)nT) * period;
  cfg.lenSec = lenSec;
  if (frameSizeSec == 0.0) frameSizeSec = period;
  cfg.frameSizeSec = frameSizeSec;
  cfg.growDyn = dyn;
  cfg.type = _type;
 // override = _override;
  manualConfig = 1;
}
*/
//----- END obsolete methods ------------

// manual configuration:
void cDataWriter::setConfig(sDmLevelConfig &_cfg, int _override)
{
  /* just ensure that we don't have corrupt values */
  _cfg.blocksizeReader = 0;
  _cfg.N = 0;
  _cfg.Nf = 0;
  _cfg.fmeta = NULL;
  _cfg.finalised = 0;
  _cfg.blocksizeIsSet = 0;
  _cfg.namesAreSet = 0;
  /* some last sanity checks: */
  if (_cfg.nT < 2) _cfg.nT = 2;
  if (_cfg.T < 0.0) _cfg.T = 0.0;
  if ((_cfg.frameSizeSec <= 0.0)&&(_cfg.T > 0.0)) _cfg.frameSizeSec = _cfg.T;
  if (_cfg.blocksizeWriter < 1) _cfg.blocksizeWriter = 1;

  cfg.updateFrom(_cfg);
  override = _override;
  manualConfig = 1;
}

void cDataWriter::setBuffersize(long nT)
{
  cfg.nT = nT;
  override_nT = 1;
}

int cDataWriter::myRegisterInstance(int *runMe)
{
  const char * tn = getComponentInstanceType(dmInstName);
  if (tn == NULL) {
    SMILE_IWRN(4,"cannot yet find dataMemory component '%s'!",dmInstName);
    return 0;
  }
  if (!strcmp(tn, COMPONENT_NAME_CDATAMEMORY)) {
    dm = (cDataMemory *)getComponentInstance(dmInstName);
    if (dm == NULL) {
      SMILE_IERR(1,"dataMemory instance dmInstance='%s' was not found in componentManager!",dmInstName);
//      COMP_ERR("failed to register!");
      return 0;
    }
  } else { // not datamemory type..
    if (dm == NULL) {
      SMILE_IERR(1,"dmInstance='%s' -> not of type %s (dataMemory)!",dmInstName,COMPONENT_NAME_CDATAMEMORY);
//      COMP_ERR("failed to register!");
      return 0;
    }
  }

  dm->registerWriteRequest(dmLevel,getInstName());

  return 1;
}

/* create and configure writer level */
// level config can be set:
//   manually by setConfig, etc.  (usually used by dataProcessors to set output level config to input level config)
//                                (this method is also used by dataSources to configure buffersize/blocksize)
//   if not set manually from the levelconf struct in the config (default values)
//   or, if explicitly specified in the config, from the levelconf values wich will overwrite the manual config values
int cDataWriter::myConfigureInstance()
{
  cfg.noHang = getInt("levelconf.noHang");

  // TODO: better control of manual config overwriting levelconf and vice versa ...
  //if (!override) {

    if (isSet("levelconf.T")||(!manualConfig)) cfg.T = getDouble("levelconf.T");
    if (isSet("levelconf.lenSec")||(!manualConfig)) {
      cfg.lenSec = getDouble("levelconf.lenSec");
      if (cfg.T != 0.0) 
        cfg.nT = (int)(cfg.lenSec / cfg.T)+1;
    }
    if (isSet("levelconf.frameSizeSec")||(!manualConfig)) cfg.frameSizeSec = getDouble("levelconf.frameSizeSec");

//    if (!override_nT) {
      if (isSet("levelconf.nT")||(!manualConfig)) {
        cfg.nT = getInt("levelconf.nT");
      }
    //}

    if (isSet("levelconf.growDyn")||(!manualConfig)) cfg.growDyn = getInt("levelconf.growDyn");
    if (isSet("levelconf.isRb")||(!manualConfig)) cfg.isRb = getInt("levelconf.isRb");
  
    if (isSet("levelconf.type")||(!manualConfig)) {
      const char *tp = getStr("levelconf.type");
      if (tp!=NULL) {
        if (!strcmp(tp,"float")) { cfg.type = DMEM_FLOAT; }
        else if (!strcmp(tp,"int")) { cfg.type = DMEM_INT; }
          else if (!strcmp(tp,"integer")) { cfg.type = DMEM_INT; }
      }
    } 

//  }

  // this will create the level specified, if it not already exists (then a warning will be issued by the dataMemory: multiple writers)
  level = dm->addLevel((sDmLevelConfig *)&cfg, dmLevel);
  if (level>=0) { return 1; }

  SMILE_IERR(2,"configureInstance: error adding level '%s' to data memory instance '%s'!",dmLevel,dmInstName);
  return 0;
}



// set the array name offset of last field that was added
void cDataWriter::setArrNameOffset(int arrNameOffset) 
{
  dm->setArrNameOffset(level, arrNameOffset);
}

// this function may be called only before finalise instance, i.e. after configure instance
int cDataWriter::addField(const char*_name, int _N, int arrNameOffset)
{
  if (_name != NULL) {
    int r = dm->addField(level,_name,_N, arrNameOffset);
    if (r) cfg.namesAreSet++;
    return r;
  }
  else return -1;
}

int cDataWriter::myFinaliseInstance()
{
  // check if level names have been set...?
  if (cfg.namesAreSet <= 0) {
    SMILE_IERR(2,"finaliseInstance: no names (fields) were set for dmLevel='%s'",dmLevel);
    return 0;
  }

  // indicate to datamemory that the names have been completely set
  dm->fixateLevel(level);

  const sDmLevelConfig *c = dm->getLevelConfig(level);
  if (c!=NULL) 
    cfg.updateFrom(*c);

  SMILE_IDBG(4,"successfully finalised dataWriter, dmLevel='%s' level=%i in memory '%s'",dmLevel,level,dmInstName);
  
  return 1;
}

// ---
// absolute position write functions:
int cDataWriter::setFrame(long vIdx, const cVector *vec, int special)
{
  return dm->setFrame(level, vIdx, vec, special);
}

int cDataWriter::setMatrix(long vIdx, const cMatrix *mat, int special)
{
  return dm->setMatrix(level, vIdx, mat, special);
}

// sequential write functions: write next frame(s)
int cDataWriter::setNextFrame(const cVector *vec)  // append at end in dataMemory level
{ 
  return setFrame(0, vec, DMEM_IDX_CURW);
}

int cDataWriter::setNextMatrix(const cMatrix *mat)   // append at end in dataMemory (no overlap)
{
  return setMatrix(0, mat, DMEM_IDX_CURW);
}

int cDataWriter::checkWrite(long len)
{
  const sDmLevelConfig *c = dm->getLevelConfig(level);
  if (c!=NULL) {
    if ((c->growDyn)&&(!(c->isRb))) return 1; // if growDyn, a write should always succeed, except for that we run out of memory
    // if nReaders in write level is 0 (dead end), then return 1 if noHang == 1 in write level
    if (c->noHang == 2) return 1;
    
    //printf("'%s' checkwrite : %i %i\n",getInstName(),dm->getNreaders(level),c->noHang);
    if ((dm->getNreaders(level) <= 0) && (c->noHang==1)) {
      return 1;
    }
  }

  return ( dm->getNFree(level) >= len );
}

/*

int cDataWriter::getLevelN()   // number of elements
{
  const sDmLevelConfig *c = dm->getLevelConfig(level);
  if (c!=NULL) return c->N;
  else return 0;
}

int cDataWriter::getLevelNf()   // number of fields
{
  const sDmLevelConfig *c = dm->getLevelConfig(level);
  if ((c!=NULL)&&(c->fmeta != NULL)) return c->fmeta->N;
  else return 0;
}

double cDataWriter::getLevelT()   // frame period (or 0.0 for unperiodic)
{
  const sDmLevelConfig *c = dm->getLevelConfig(level);
  if (c!=NULL) return c->T;
  else return -1.0;
}

const FrameMetaInfo * cDataWriter::getFrameMetaInfo()    // names of fields, etc.
{
  const sDmLevelConfig *c = dm->getLevelConfig(level);
  if (c!=NULL) return c->fmeta;
  else return NULL;
}

*/