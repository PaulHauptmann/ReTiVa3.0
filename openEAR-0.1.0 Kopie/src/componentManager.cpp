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


/*

central object to manage all components

componentManager registers a config type, which specifies the component list.
Example:

[componentInstances:cComponentManager]
instance[myWavReader].type = cWavReader
instance[myWavReader].configInstance = wavReader1Config
instance[myXYZcomp].type = cCompType
...



*********init procedure:

create componentManager
register all components (from componentlist, or later from dyn. libs)
load smile and componentManger config
create component instances (datamemory, readers, writers, and the rest)
configure all instances (once all instances are ready) [writers register dataMemory levels, etc.,]
finalise all instances (if all instances are configured, datamemory finalises here! (datamemory does sanity check on r/w level usage during finalise)

tick() loop

?? -> exit? external signal(ctrl+c, message, etc.) + component exception or state..? (e.g. EOF input file)
OR: no progress for X ticks..?
=> implement mechanism for signalling end-of-processing (EOP) to component manager (e.g. new exception type?)
PROBLEM: if end-of-input is reached, then there might be more processing required till we are completely finished...
(only components without a data reader can signal EOP?)
THUS: no progress for X ticks..AFTER at least one component has signalled EOP?

???? support reconf via componentManager ????
*/

#include <componentManager.hpp>


//TODO:
/*
handle component creation, config, and finalisation better, give more suitable (success/fail) debug messages
halt on config and/or finalise errors
allow manual configuration of components by calling create, config, and finalise seperately
(however, also allow for single call setup (default!))
*/


// global component list: -----------------
/* list all built-in components here... 
Also be sure to include the necessary component header files
*/


// basic functionality / SMILE API
#include <dataMemory.hpp>
#include <dataReader.hpp>
#include <dataWriter.hpp>
#include <dataSource.hpp>
#include <dataSink.hpp>
#include <dataProcessor.hpp>
#include <dataSelector.hpp>
#include <vectorProcessor.hpp>
#include <windowProcessor.hpp>
#include <winToVecProcessor.hpp>

// examples:
#include <exampleSource.hpp>
#include <exampleSink.hpp>
#include <exampleProcessor.hpp>

// basic operations:
#include <buffer.hpp>
#include <vectorConcat.hpp>
#include <windower.hpp>
#include <framer.hpp>

#include <fullinputMean.hpp>
// sources:
#include <waveSource.hpp>
#include <arffSource.hpp>
#include <portaudioSource.hpp>
// network sources:
#include <activeMqSource.hpp>

// sinks:
#include <csvSink.hpp>
#include <datadumpSink.hpp>
#include <arffSink.hpp>
#include <htkSink.hpp>
#include <libsvmSink.hpp>
#include <waveSink.hpp>
#include <waveSinkCut.hpp>


// live sinks (classifiers):
#include <libsvmliveSink.hpp>
#include <tumkwsaSink.hpp>
#include <tumkwsjSink.hpp>
#include <portaudioSink.hpp>
#include <nnlPlugin.hpp>
// network sinks:
#include <activeMqSink.hpp>

#include <portaudioDuplex.hpp>
#include <portaudioDuplexS.hpp>
#include <portaudioDuplexD.hpp>


// low-level signal processing:
#include <transformFft.hpp>
#include <fftmagphase.hpp>
#include <amdf.hpp>
#include <acf.hpp>
#include <preemphasis.hpp>
#include <vectorPreemphasis.hpp>  // htk compatible (sloppy) pre-emphasis
#include <mzcr.hpp>
#include <echoAttenuator.hpp>
#include <echoCanceller.hpp>
#include <speexPreprocess.hpp>
#include <speexResample.hpp>

// LLD (low-level descriptors):
#include <energy.hpp>
#include <intensity.hpp>
#include <dbA.hpp>
#include <melspec.hpp>
#include <mfcc.hpp>       // mfcc from melspec
#include <tonespec.hpp>
#include <tonefilt.hpp>
#include <chroma.hpp>
#include <chromaFeatures.hpp>
#include <spectral.hpp>
#include <pitchACF.hpp>
#include <lpc.hpp>
#include <lsp.hpp>

// filters:
#include <vecGlMean.hpp>  // e.g. CMS for MFCC
#include <vectorMVStd.hpp>
#include <deltaRegression.hpp>
#include <contourSmoother.hpp>

// functionals:
#include <functionals.hpp>
#include <functionalsVecToVec.hpp>
#include <functionalExtremes.hpp>
#include <functionalMeans.hpp>
#include <functionalPeaks.hpp>
#include <functionalSegments.hpp>
#include <functionalMoments.hpp>
#include <functionalCrossings.hpp>
#include <functionalPercentiles.hpp>
#include <functionalRegression.hpp>
#include <functionalTimes.hpp>
#include <functionalDCT.hpp>

// other:
#include <turnDetector.hpp>
#include <volanalyse.hpp>
#include <fingerprint.hpp>
#include <semaineEmmaSender.hpp>


DLLEXPORT const registerFunction componentlist[] = {
  cDataMemory::registerComponent,
  cDataWriter::registerComponent,
  cDataReader::registerComponent,
  cDataSource::registerComponent,
  cDataSink::registerComponent,
  cDataProcessor::registerComponent,
  cDataSelector::registerComponent,
  cVectorProcessor::registerComponent,
  cWindowProcessor::registerComponent,
  cWinToVecProcessor::registerComponent,

  cExampleSource::registerComponent,
  cExampleSink::registerComponent,
  cExampleProcessor::registerComponent,

  cBuffer::registerComponent,
  cVectorConcat::registerComponent,

  cWaveSource::registerComponent,
  cArffSource::registerComponent,

#ifdef HAVE_PORTAUDIO
  cPortaudioSource::registerComponent,
  cPortaudioSink::registerComponent,
  cPortaudioDuplex::registerComponent,
  cPortaudioDuplexS::registerComponent,
  cPortaudioDuplexD::registerComponent,
#endif

  cArffSink::registerComponent,
  cLibsvmSink::registerComponent,
  cCsvSink::registerComponent,
  cHtkSink::registerComponent,
  cDatadumpSink::registerComponent,
  cWaveSink::registerComponent,
  cWaveSinkCut::registerComponent,

  cLibsvmLiveSink::registerComponent,

#ifdef HAVE_RTNNLLIB
  nnlPlugin::registerComponent,
#endif

#ifdef HAVE_ATKLIB
  cTumkwsaSink::registerComponent,
#endif

#ifdef HAVE_JULIUSLIB
  cTumkwsjSink::registerComponent,
#endif

#ifdef HAVE_SEMAINEAPI
  cActiveMqSink::registerComponent,
  cActiveMqSource::registerComponent,
  cSemaineEmmaSender::registerComponent,
#endif

  cFramer::registerComponent,
  cWindower::registerComponent,

  cFullinputMean::registerComponent,
  cVecGlMean::registerComponent,
  cVectorMVStd::registerComponent,
  cTurnDetector::registerComponent,
  cEnergy::registerComponent,
  cIntensity::registerComponent,
  cTransformFFT::registerComponent,
  cFFTmagphase::registerComponent,
  cDbA::registerComponent,
  cMelspec::registerComponent,
  cTonespec::registerComponent,
  cTonefilt::registerComponent,
  cMfcc::registerComponent,
  cChroma::registerComponent,
  cChromaFeatures::registerComponent,
  cSpectral::registerComponent,

  cMZcr::registerComponent,
  cLpc::registerComponent,
  cLsp::registerComponent,

#ifdef HAVE_SPEEXLIB
  cEchoCanceller::registerComponent,
  cSpeexPreprocess::registerComponent,
  cSpeexResample::registerComponent,
#endif
  cEchoAttenuator::registerComponent,
  cAmdf::registerComponent,
  cAcf::registerComponent,

  cPitchACF::registerComponent,

  cDeltaRegression::registerComponent,
  cContourSmoother::registerComponent,
  cPreemphasis::registerComponent,
  cVectorPreemphasis::registerComponent,

  cFunctionals::registerComponent,
  cFunctionalsVecToVec::registerComponent,

  cFunctionalExtremes::registerComponent,
  cFunctionalMeans::registerComponent,
  cFunctionalPeaks::registerComponent,
  cFunctionalSegments::registerComponent,
  cFunctionalMoments::registerComponent,
  cFunctionalCrossings::registerComponent,
  cFunctionalPercentiles::registerComponent,
  cFunctionalRegression::registerComponent,
  cFunctionalTimes::registerComponent,
  cFunctionalDCT::registerComponent,

  cVolanalyse::registerComponent,
  cFingerprint::registerComponent,

  NULL   // the last element must always be NULL !
};

#define MODULE "cComponentManager"

//-----------------------------------------



/************************/

void cComponentManager::registerType(cConfigManager *_confman) {
  //confman = _confman;
  if (_confman != NULL) {
    ConfigType *comp = new ConfigType("cComponentManagerInst");
    if (comp == NULL) OUT_OF_MEMORY;
    comp->setField( "type", "name of component type to create an instance of", (char*)NULL);
    comp->setField( "configInstance", "config instance to connect to component instance (UNTESTED?)", (char*)NULL);
    comp->setField( "threadId", "thread nr. to run this component in (default = -1: either run in 1st thread or automatically run each component in one thread if nThread==0)", -1);

    ConfigType *complist = new ConfigType( "cComponentManager" );
    if (complist == NULL) OUT_OF_MEMORY;
    complist->setField( "instance", "Associative array storing component list.\n   Array indicies are the instance names.",
      comp, 1 );
    complist->setField( "printLevelStats", "1 = print detailed information about data memory level configuration, 2 = print even more details (?)",1);
    complist->setField( "nThreads", "number of threads to run (0=auto(=one thread per component), >0 = actual number of threads",1);
    ConfigInstance *Tdflt = new ConfigInstance( "cComponentManagerInst", complist, 1 );
    _confman->registerType(Tdflt);
    //confman->registerType( complist );
  } else {
    SMILE_ERR(1,"cannot register component manager config type! _confman is NULL in registerType()!");
  }
}

/********************/

// sComponentInfo *comps; // component types

int cComponentManager::registerComponent(sComponentInfo *c) // register a component type and free the sComponentInfo struct memory
{
  if (c!=NULL) {
    // find existing:
    int t = findComponentType(c->componentName);
    if (t == -1) {
      if (nCompTs >= nCompTsAlloc) { // realloc
        sComponentInfo *_compTs = (sComponentInfo *)crealloc(compTs, (nCompTs+COMPONENTMANAGER_DEFAULT_NCOMPS)*sizeof(sComponentInfo), nCompTsAlloc*sizeof(sComponentInfo));
        if (_compTs == NULL) OUT_OF_MEMORY;
        compTs = _compTs;
        nCompTsAlloc = (nCompTs+COMPONENTMANAGER_DEFAULT_NCOMPS);
      }
      t = nCompTs++;
      memcpy(compTs+t, c, sizeof(sComponentInfo));
      compTs[t].next = NULL;
      SMILE_MSG(3,"registered component type '%s' with id %i", compTs[t].componentName, t);
    } else {
      memcpy(compTs+t, c, sizeof(sComponentInfo));
      compTs[t].next = NULL;
      SMILE_MSG(3,"re-registered component type '%s' with id %i", compTs[t].componentName, t);
    }
    delete c;
    return t;
  }
  return -1;
}

int cComponentManager::findComponentType(const char *_type)
{
  int i;
  if (compTs == NULL) return -1;
  for (i=0; i<nCompTs; i++) {
    if (!strcmp(_type, compTs[i].componentName)) {
      SMILE_DBG(5,"findComponentType: found componentType '%s' at index %i", _type, i);
      return i;
    }
  }
  return -1;
}

const char * cComponentManager::getComponentType(int i, int filter, int *isAbstract, int *isNoDmem) // get name of component Type "i". abstract=1 = include abstract types (if abstract = 0 , then NULL will be returned if the type is abstract), or you may use the isAbstract flag, which is set by this function
{
  if ( (i>=0)&&(i<nCompTs) ) {
    if (isAbstract != NULL) *isAbstract = compTs[i].abstract;
    if (isNoDmem != NULL) *isNoDmem = compTs[i].noDmem;
    if (filter == 0) { // filter = 0: return all components
      return compTs[i].componentName;
    } else {
      if (filter == 1) {  // filter=1 : return non-abstract components
        if (compTs[i].abstract) return NULL;
        else return compTs[i].componentName;
      } else if (filter==2) { // filter = 2: return only dmem interface componenets (non-abstract and non-noDmem)
        if ((compTs[i].abstract)||(compTs[i].noDmem)) return NULL;
        else return compTs[i].componentName;
      }
    }
  } else {
    return NULL;
  }
  return NULL;
}

const char * cComponentManager::getComponentDescr(int i) // get name of component Type "i". abstract=1 = include abstract types (if abstract = 0 , then NULL will be returned if the type is abstract), or you may use the isAbstract flag, which is set by this function
{
  if ( (i>=0)&&(i<nCompTs) ) {
    return compTs[i].description;
  } else { return NULL; }
}

#ifdef SMILE_SUPPORT_PLUGINS

int cComponentManager::checkPluginFilename(const char * str)
{
  const char * dot = strrchr(str,'.');
#ifdef __WINDOWS
  const char * ending = "dll";
  int n = 3;
#else
  const char * ending = "so";
  int n = 2;
#endif
  if (dot != NULL) {
    dot++;
    if (!strncasecmp(dot,ending,n)) return 1;
  }
  //TODO: find .so/.dll files even if a version number e.g. .so.0.0.1 is appended!

  return 0;
}


#ifndef __WINDOWS

//#include <windows.h>
//#include <tchar.h>
//#include <string.h>
//#include <strsafe.h>

//#else

// unix/gnu
#include <sys/types.h>
#include <dirent.h>
#include <dlfcn.h>

#endif


int cComponentManager::loadPlugin(const char * path, const char * fname)
{
  //sComponentInfo * registerComponent(cConfigManager *_confman, cComponentManager *_compman)
  //sComponentInfo * (*regFn)(cConfigManager *_confman, cComponentManager *_compman);
  registerFunction regFn;

  char * fullname;
  if (path != NULL) {
#ifdef __WINDOWS
    fullname = myvprint("%s\\%s",path,fname);
#else
    fullname = myvprint("%s/%s",path,fname);
#endif
  } else {
    fullname = myvprint("%s",fname);
  }

#ifdef __WINDOWS
  HINSTANCE lib_handle;
  lib_handle = LoadLibrary(TEXT(fullname));

  // If the handle is valid, try to get the function address.
  if (lib_handle != NULL) {
    regFn = (registerFunction) GetProcAddress(lib_handle, "registerPluginComponent");
    // If the function address is valid, call the function.
    if (regFn == NULL) {
      SMILE_ERR(1, "error registering plugin '%s' (symbol 'registerPluginComponent' not found)",fullname);
      FreeLibrary(lib_handle);
      return 0;
    }
  } else {
    SMILE_ERR(1,"cannot open library '%s' : LoadLibrary() failed!",fullname);
    return 0;
  }

#else
  char *error;
  void *lib_handle;

  lib_handle = dlopen(fullname, RTLD_LAZY);
  if (!lib_handle) {
    SMILE_ERR(1, "cannot open plugin '%s' : '%s'", fullname, dlerror());
    return 0;
  }

  regFn = (registerFunction)dlsym(lib_handle, "registerPluginComponent");
  if ( ((error = dlerror()) != NULL) || (regFn == NULL)) {
    SMILE_ERR(1, "error registering plugin '%s' (symbol 'registerPluginComponent' not found): '%s'",fullname, error);
    dlclose(lib_handle);
    return 0;
  }
#endif

  SMILE_MSG(4, "found registerPluginComponent() in '%s'",fullname);

  free(fullname);
  if (nPluginHandles >= nPluginHandlesAlloc) {
#ifdef __WINDOWS
    handlelist = (HINSTANCE*)crealloc(handlelist, (nPluginHandlesAlloc+COMPONENTMANAGER_DEFAULT_NCOMPS)*sizeof(HINSTANCE), (nPluginHandlesAlloc)*sizeof(HINSTANCE) );
#else
    handlelist = (void**)crealloc(handlelist, (nPluginHandlesAlloc+COMPONENTMANAGER_DEFAULT_NCOMPS)*sizeof(void*), (nPluginHandlesAlloc)*sizeof(void*) );
#endif
    regFnlist =  (registerFunction *)crealloc((void *)regFnlist, (nPluginHandlesAlloc+COMPONENTMANAGER_DEFAULT_NCOMPS)*sizeof(registerFunction), (nPluginHandlesAlloc)*sizeof(registerFunction) );
    if (handlelist == NULL) OUT_OF_MEMORY;
    if (regFnlist == NULL) OUT_OF_MEMORY;
    nPluginHandlesAlloc += COMPONENTMANAGER_DEFAULT_NCOMPS;
  }
  handlelist[nPluginHandles] = lib_handle;
  regFnlist[nPluginHandles++] = regFn;

  return 1;
}


int cComponentManager::registerPlugins()
{
  int nPlugins = 0;
  nPluginHandles = 0;
  nPluginHandlesAlloc = 0;

  // scan plugins in plugin-path:
#ifdef __WINDOWS
  // TODO: config file option "pluginpath" and "pluginlist"
  const char * pluginpath = ".\\plugins";

  // WIN: use FindFirstFile, FindNextFile, FindClose
  WIN32_FIND_DATA ffd;
  HANDLE hFind = INVALID_HANDLE_VALUE;
  char szDir[MAX_PATH];
  DWORD dwError=0;

  if (strlen(pluginpath) > (MAX_PATH - 2)) {
    SMILE_ERR(1,"Plugin-directory path '%s' is too long for windows systems....",pluginpath);
    return 0;
  }

  // Prepare string for use with FindFile functions.  First, copy the
  // string to a buffer, then append '\*' to the directory name.

#ifdef __MINGW32
  strncpy(szDir, pluginpath, MAX_PATH);
#else
  strcpy_s(szDir, MAX_PATH, pluginpath);
#endif
  strncat(szDir, "\\*", MAX_PATH);

  hFind = FindFirstFile(szDir, &ffd);
  if (INVALID_HANDLE_VALUE == hFind) {
    SMILE_ERR(1,"cannot find files in plugin directory '%s'!",pluginpath);
    return 0;
  }

  // List all the files in the directory with some info about them.
  do {
    if (!(ffd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
      if (checkPluginFilename(ffd.cFileName)) {
        SMILE_MSG(2,"found plugin : '%s'",ffd.cFileName);
        // load the plugin:
//#ifdef __WINDOWS
        if (loadPlugin(pluginpath, ffd.cFileName)) nPlugins++;
//#else
        //if (loadPlugin(NULL, ffd.cFileName)) nPlugins++;
//#endif
      }
    }
  }
  while (FindNextFile(hFind, &ffd) != 0);

  dwError = GetLastError();
  if (dwError != ERROR_NO_MORE_FILES) {
    SMILE_ERR(1,"error reading contents of plugin-directory '%s' (nPlugins=%i plugins loaded)! ",pluginpath,nPlugins);
    FindClose(hFind);
    return nPlugins;
  }
  FindClose(hFind);

#else  // UNIX:
  // TODO: config file option "pluginpath" and "pluginlist"
  const char * pluginpath = "./plugins";

  DIR *dp;
  struct dirent *dirp;
  if((dp  = opendir(pluginpath)) == NULL) {
    SMILE_ERR(3,"cannot open plugin directory '%s' for reading!",pluginpath);
    return 0;
  }

  while ((dirp = readdir(dp)) != NULL) {
    if (checkPluginFilename(dirp->d_name)) { // TODO: skip directories!
      SMILE_MSG(2,"found plugin : '%s'",dirp->d_name);
      // load the plugin:
      if (loadPlugin(pluginpath, dirp->d_name)) nPlugins++;
    }
  }
  closedir(dp);
#endif

  if (nPlugins == 0) return 0;

  int i;
  int nAgain=0, nReg=0;
  int regIter = MAX_REG_ITER;

  int *regDone = (int *) calloc(1,sizeof(int)*nPlugins);

  if (printPlugins) {
    SMILE_PRINT (" == List of detected plugins: ==");
  }

  do {

    for (i=0; i<nPlugins; i++) {
      if (!(regDone[i])) {
        sComponentInfo *c = (regFnlist[i])(confman,this);

        do {

          if ((c!=NULL)&&(printPlugins)) {
            SMILE_PRINT(" plugin '%s' : '%s'",c->componentName,c->description);
          }

          sComponentInfo *nextc;
          if (c!=NULL) nextc = c->next;

          int t = registerComponent( c );

          if ( (t>=0) && (t < nCompTsAlloc)) {
            if (compTs[t].registerAgain) { nAgain++; }
            else { nReg++; regDone[i] = 1; }
          }
          c = nextc;
        } while (c!=NULL);
      }
    }

#ifdef DEBUG
    //printf("reg round %i - nAgain %i\n",regIter,nAgain);
    if (nAgain > 0)
      SMILE_DBG(3,"%i of %i plugin-components requested re-register in round %i",nAgain,nAgain+nReg,MAX_REG_ITER-regIter+1);
#endif

  } while ((nAgain > 0 )&&(regIter-- > 0));
  if (printPlugins) {
    SMILE_PRINT (" ===============================");
  }

  free(regDone);

  return nReg;
}
#endif

// register component types by scanning given struct
int cComponentManager::registerComponentTypes(const registerFunction _clist[]) 
{
  int i=0;
  int nAgain, nReg=0;
  int regIter = MAX_REG_ITER;

  int nc=0;
  while (_clist[i] != NULL) { nc++; i++; }
  i=0;
  int *regDone = (int *) calloc(1,sizeof(int)*nc);

  if (_clist != NULL) {
    do {
      nAgain = 0; i=0;
      //TODO: remember already registered componentes right here.... do not call registerComponent twice!
      while (_clist[i] != NULL) {
        if (!(regDone[i])) {
          int t = registerComponent( (_clist[i])(confman,this) );
          if ( (t>=0) && (t < nCompTsAlloc)) {
            if (compTs[t].registerAgain) { nAgain++; }
            else { nReg++; regDone[i] = 1; }
          }
        }
        i++;
      }
#ifdef DEBUG
      //printf("reg round %i - nAgain %i\n",regIter,nAgain);
      if (nAgain > 0)
        SMILE_DBG(3,"%i of %i components requested re-register in round %i",nAgain,nAgain+nReg,MAX_REG_ITER-regIter+1);
#endif
    } while ((nAgain > 0 )&&(regIter-- > 0));
    if ((regIter == 0)&&(nAgain > 0)) {
      free(regDone);
      COMP_ERR("%i of %i components could not register successfully during %i registration iterations",nAgain,nAgain+nReg,MAX_REG_ITER);
    } else
      SMILE_MSG(2,"successfully registered %i component types.",nReg);
  }
  free(regDone);

  // now register plug-in components...
  nReg += registerPlugins();

  return nReg;
}

int cComponentManager::printComponentList(int filter, int details)
{
  int nTp = getNtypes();
  int i,j=0;
  //  if (details) {
  SMILE_PRINT("==> The following %i components are currently registered in openSMILE:\n",nTp);
  //  }
  for (i=0; i<nTp; i++) {
    const char * tp = getComponentType(i,filter);
    if (tp!=NULL) {
      if (details) {
        SMILE_PRINT(" +++ '%s' +++",tp);
        SMILE_PRINT("   %s\n",getComponentDescr(i));
        // TODO: print if component is built in OR dll registered...
      } else {
        SMILE_PRINT("  '%s'",tp);
      }
    }
  }
  return nTp;
}

cComponentManager::cComponentManager(cConfigManager *_confman, const registerFunction _clist[]) :
nComponents(0),
lastComponent(0),
nComponentsAlloc(0),
ready(0),
confman(_confman),
nCompTs(0),
handlelist(NULL),
regFnlist(NULL),
nCompTsAlloc(0),
nWaiting(0),
nActive(0),
printPlugins(1),
//  threadNRun(NULL),
globalRunState(0),
compTs(NULL),
abortRequest(0),
componentThreadId(NULL),
EOI(0),
isConfigured(0), isFinalised(0), printLevelStats(0),
messageCounter(0)
{
  if (confman == NULL) COMP_ERR("cannot create component manager with _confman == NULL!");
  cComponentManager::confman = _confman;

  smileMutexCreate(messageMtx);
  smileMutexCreate(abortMtx);

  // register components (component types)
  registerComponentTypes(_clist);

  // register our config type:
  cComponentManager::registerType(confman);

  component = (cSmileComponent **) calloc(1,sizeof(cSmileComponent *) * COMPONENTMANAGER_DEFAULT_NCOMPS);
  componentInstTs = (char **) calloc(1,sizeof(char *) * COMPONENTMANAGER_DEFAULT_NCOMPS);
  componentThreadId = (int*) calloc(1,sizeof(int *) * COMPONENTMANAGER_DEFAULT_NCOMPS);
  if (component == NULL) OUT_OF_MEMORY;
  if (componentInstTs == NULL) OUT_OF_MEMORY;
  if (componentThreadId == NULL) OUT_OF_MEMORY;
  nComponentsAlloc = COMPONENTMANAGER_DEFAULT_NCOMPS;

  // get system start time
  gettimeofday(&startTime,NULL);
}

int cComponentManager::compIsDm(const char *_compn)
{
  return (!strcmp(_compn,COMPONENT_NAME_CDATAMEMORY)); 
}

int cComponentManager::ciRegisterComps(int _dm)
{
#ifdef DEBUG
  if (_dm == 0) {
    SMILE_DBG(2,"==> createInstances: REGISTER PHASE (components) <==");
  } else {
    SMILE_DBG(2,"==> createInstances: REGISTER PHASE (dataMemories) <==");
  }
  SMILE_DBG(2,"    %i instances in total (max. %i iterations)",  nComponents, MAX_REGI_ITER );
#endif

  int it,i;
  int nDone = 0; 
  int nDef = 0;
  int nIgn = 0;

  for (it=0; it<MAX_REGI_ITER; it++) {
    nDone = 0; 
    nDef = 0;
    nIgn = 0;

    // register all components 
    for (i=0; i<lastComponent; i++) {
      if (component[i]!=NULL) {
        if (compIsDm(component[i]->getTypeName()) == _dm) {

          if (component[i]->registerInstance()) { // TODO: save runMe config in componentManager..
            nDone++;
            SMILE_DBG(3,"registered component instance '%s' (type '%s'), index %i",component[i]->getInstName(),component[i]->getTypeName(),i);
          } else {
            nDef++;
            SMILE_DBG(3,"component instance '%s' (type '%s'), index %i, could not be registered",component[i]->getInstName(),component[i]->getTypeName(),i);
          }

        } else {
          nIgn++;
        }
      }
    }

    if (nDef == 0) {
      if (_dm == 0) 
        SMILE_MSG(3,"successfully registered %i of %i component instances (non dataMemory type)", nDone, nComponents-nIgn );
      else
        SMILE_MSG(3,"successfully registered %i of %i dataMemory instances", nDone, nComponents-nIgn );
      break; // else: continue configuration process for MAX_REGI_ITER
    } else {
      SMILE_DBG(2,"need to re-register %i components after iteration %i",nDef,it);
    }
  }

  return (nDef);
}

int cComponentManager::ciConfigureComps(int _dm)
{
#ifdef DEBUG
  if (_dm == 0) {
    SMILE_DBG(2,"==> createInstances: CONFIGURE PHASE (components) <==");
  } else {
    SMILE_DBG(2,"==> createInstances: CONFIGURE PHASE (dataMemories) <==");
  }
  SMILE_DBG(2,"    %i instances in total (max. %i iterations)",  nComponents, MAX_CONF_ITER );
#endif

  int it,i;
  int nDone = 0; 
  int nDef = 0;
  int nIgn = 0;

  for (it=0; it<MAX_CONF_ITER; it++) {
    nDone = 0; 
    nDef = 0;
    nIgn = 0;

    // register all components 
    for (i=0; i<lastComponent; i++) {
      if (component[i]!=NULL) {
        if (compIsDm(component[i]->getTypeName()) == _dm) {

          if (component[i]->configureInstance()) {
            nDone++;
            SMILE_DBG(3,"configured component instance '%s' (type '%s'), index %i",component[i]->getInstName(),component[i]->getTypeName(),i);
          } else {
            nDef++;
            SMILE_DBG(3,"component instance '%s' (type '%s'), index %i, could not be configured (yet)",component[i]->getInstName(),component[i]->getTypeName(),i);
          }

        } else {
          nIgn++;
        }
      }
    }

    if (nDef == 0) {
      if (_dm == 0) 
        SMILE_MSG(3,"successfully configured %i of %i component instances (non dataMemory type)", nDone, nComponents-nIgn );
      else
        SMILE_MSG(3,"successfully configured %i of %i dataMemory instances", nDone, nComponents-nIgn );
      break; // else: continue configuration process for MAX_CONF_ITER
    } else {
      SMILE_DBG(2,"need to re-configure %i components after iteration %i",nDef,it);
    }
  }

  return (nDef);
}

int cComponentManager::ciFinaliseComps(int _dm, int *_n)
{
#ifdef DEBUG
  if (_dm == 0) {
    SMILE_DBG(2,"==> createInstances: FINALISE PHASE (components) <==");
  } else {
    SMILE_DBG(2,"==> createInstances: FINALISE PHASE (dataMemories) <==");
  }
  SMILE_DBG(2,"    %i instances in total (max. %i iterations)",  nComponents, MAX_FIN_ITER );
#endif

  int it,i;
  int nDone = 0; 
  int nDef = 0;
  int nIgn = 0;

  for (it=0; it<MAX_FIN_ITER; it++) {
    nDone = 0; 
    nDef = 0;
    nIgn = 0;

    // finalise components 
    for (i=0; i<lastComponent; i++) {
      if (component[i]!=NULL) {
        if (compIsDm(component[i]->getTypeName()) == _dm) {

          if (component[i]->finaliseInstance()) {
            nDone++;
            SMILE_DBG(3,"finalised component instance '%s' (type '%s'), index %i",component[i]->getInstName(),component[i]->getTypeName(),i);
          } else {
            nDef++;
            SMILE_DBG(3,"component instance '%s' (type '%s'), index %i, could not be finalised",component[i]->getInstName(),component[i]->getTypeName(),i);
          }

          if ( (_dm)&&(printLevelStats) ) {
            ((cDataMemory *)component[i])->printDmLevelStats(printLevelStats);
          }
        } else {
          nIgn++;
        }
      }
    }

    if (nDef == 0) {
      if (_dm == 0) 
        SMILE_MSG(3,"successfully finalised %i of %i component instances (non dataMemory type)", nDone, nComponents-nIgn );
      else
        SMILE_MSG(3,"successfully finalised %i of %i dataMemory instances", nDone, nComponents-nIgn );
      break; // else: continue configuration process for MAX_FIN_ITER
    } else {
      SMILE_DBG(2,"need to re-finalise %i components after iteration %i",nDef,it);
    }
  }

  if (_n != NULL) *_n = nDone;
  return (nDef);
}

// configure and finalise in turns..
int cComponentManager::ciConfFinComps(int _dm, int *_n)
{
#ifdef DEBUG
  if (_dm == 0) {
    SMILE_DBG(2,"==> createInstances: CONFIGURE PHASE (components) <==");
  } else {
    SMILE_DBG(2,"==> createInstances: CONFIGURE PHASE (dataMemories) <==");
  }
  SMILE_DBG(2,"    %i instances in total (max. %i iterations)",  nComponents, MAX_CONF_ITER );
#endif

  int it,i;
  int nDone = 0; 
  int nDef = 0;
  int nIgn = 0;

  for (it=0; it<MAX_CONF_ITER; it++) {
    nDone = 0; 
    nDef = 0;
    nIgn = 0;

    // register all components 
    for (i=0; i<lastComponent; i++) {
      if (component[i]!=NULL) {
        if (compIsDm(component[i]->getTypeName()) == _dm) {

          if (component[i]->configureInstance()) {
            //nDone++;
            SMILE_DBG(3,"configured component instance '%s' (type '%s'), index %i",component[i]->getInstName(),component[i]->getTypeName(),i);
            if (component[i]->finaliseInstance()) {
              nDone++;
              SMILE_DBG(3,"configured component instance '%s' (type '%s'), index %i",component[i]->getInstName(),component[i]->getTypeName(),i);
            } else {
              nDef++;
              SMILE_DBG(3,"component instance '%s' (type '%s'), index %i, could not be configured (yet)",component[i]->getInstName(),component[i]->getTypeName(),i);
            }

          } else {
            nDef++;
            SMILE_DBG(3,"component instance '%s' (type '%s'), index %i, could not be configured (yet)",component[i]->getInstName(),component[i]->getTypeName(),i);
          }

        } else {
          nIgn++;
        }
      }
    }

    if (nDef == 0) {
      if (_dm == 0) 
        SMILE_MSG(3,"successfully configured %i of %i component instances (non dataMemory type)", nDone, nComponents-nIgn );
      else
        SMILE_MSG(3,"successfully configured %i of %i dataMemory instances", nDone, nComponents-nIgn );
      break; // else: continue configuration process for MAX_CONF_ITER
    } else {
      SMILE_DBG(2,"need to re-configure %i components after iteration %i",nDef,it);
    }
  }

  if (_n != NULL) *_n = nDone;
  return (nDef);
}

void cComponentManager::createInstances(int readConfig)
{
  /*
  create component instances (datamemory, readers, writers, and the rest)
  configure all instances (once all instances are ready) [writers register dataMemory levels, etc.,]
  finalise all instances (if all instances are configured, datamemory finalises here! (datamemory does sanity check on r/w level usage during finalise)
  */
  // load smile and componentManger config
  if (readConfig) confman->readConfig();

  char *tmp = myvprint("%s.printLevelStats",CM_CONF_INST);
  printLevelStats = confman->getInt(tmp);
  free(tmp);

  // create component instances (datamemory, readers, writers, and the rest)
  //     const char **getArrayKeys(const char *_name, int *N=NULL) const;
  int _N=0;
  tmp = myvprint("%s.instance",CM_CONF_INST);
  char **insts = confman->getArrayKeys(tmp,&_N);
  if (tmp!=NULL) free(tmp);
  if ((insts!=NULL)&&(_N>0)) {
    SMILE_DBG(2,"found %i component instances in config to create.",_N);
    int i;

    // prepare threads:
    nThreads = confman->getInt_f(myvprint("%s.nThreads",CM_CONF_INST));

    // create compnent objects and register them
    for (i=0; i<_N; i++) {
      const char *k = insts[i];
      if (k!=NULL) {
        const char *tp = confman->getStr_f(myvprint("%s.instance[%s].type",CM_CONF_INST,k));
        const char *ci = confman->getStr_f(myvprint("%s.instance[%s].configInstance",CM_CONF_INST,k));
        // check config:
        if (tp == NULL) CONF_INVALID_ERR("%s.instance[%s].type is missing!",CM_CONF_INST,k);
        if (ci == NULL) ci = k;
        SMILE_DBG(2," adding %i. component instance: name '%s', type '%s', configInstance '%s'",i,k,tp,ci);
        int tmpId = confman->getInt_f(myvprint("%s.instance[%s].threadId",CM_CONF_INST,k));
        if (tmpId < -2) tmpId = -1;  // NOTE: threadId = -2 => do not tick this component at all!!
        if (tmpId >= nThreads) {
          CONF_INVALID_ERR("%s.instance[%s].threadId must be < %s.nThreads (first Id = 0)!",CM_CONF_INST,k,CM_CONF_INST);
        }
        int a = addComponent(k,tp,ci,tmpId);
        if (a>=0) {
          SMILE_DBG(4," added %i. component instance at index %i (lc=%i)",i,a,lastComponent);
          // set configInstance name...
          //          setConfigInstanceName..ok!
        } else {
          COMP_ERR("error during addComponent (returnVal=%i)!",a);
        }
      }
    }

    // configure and finalise components in turn:
    // 1a. register (components, NON dataMemory)
    // 1b. register (dataMemories)
    // 2a. configure (components, NON dataMemory)
    // 2b. configure (dataMemories)
    // 3a. finalise (components, NON dataMemory)
    // 3b. finalise (dataMemories)

    // we need to do this so the readers of e.g. dataProcessors can be configured after the writers for the corresponding levels have been finalised

    if (ciRegisterComps(0)) COMP_ERR("createInstances: failed registering component instances");
    if (ciRegisterComps(1)) COMP_ERR("createInstances: failed registering dataMemory instances");

    int nFinC = 0, nFinD = 0;
    if (ciConfFinComps(0,&nFinC)) COMP_ERR("createInstances: failed configuring&finalising component instances");
    //if (ciConfigureComps(0)) COMP_ERR("createInstances: failed configuring component instances");
    //if (ciFinaliseComps(0,&nFinC)) COMP_ERR("createInstances: failed finalising component instances");
    isConfigured=1;

    if (ciConfigureComps(1)) COMP_ERR("createInstances: failed configuring dataMemory instances");
    if (ciFinaliseComps(1,&nFinD)) COMP_ERR("createInstances: failed finalising dataMemory instances");
    isFinalised=1;

    SMILE_MSG(2,"successfully finished createInstances\n                                 (%i component instances were finalised, %i data memories were finalised)", nFinC, nFinD);
    ready = 1;
  }
}

int cComponentManager::getNextComponentId()
{
  if (lastComponent >= nComponentsAlloc) {  // reallocate a larger component array
    cSmileComponent **tmp;
    tmp = (cSmileComponent **) crealloc(component,
      sizeof(cSmileComponent *) * (lastComponent + COMPONENTMANAGER_DEFAULT_NCOMPS),
      sizeof(cSmileComponent *) * nComponentsAlloc);
    char **tmpn;
    tmpn = (char **) crealloc(componentInstTs,
      sizeof(char *) * (lastComponent + COMPONENTMANAGER_DEFAULT_NCOMPS),
      sizeof(char *) * nComponentsAlloc);
    int *tmpi;
    tmpi = (int *) crealloc(componentThreadId,
      sizeof(int) * (lastComponent + COMPONENTMANAGER_DEFAULT_NCOMPS),
      sizeof(int) * nComponentsAlloc);

    if (tmp == NULL) OUT_OF_MEMORY;
    if (tmpn == NULL) OUT_OF_MEMORY;
    if (tmpi == NULL) OUT_OF_MEMORY;
    nComponentsAlloc = (lastComponent + COMPONENTMANAGER_DEFAULT_NCOMPS);
    component = tmp;
    componentInstTs = tmpn;
    componentThreadId = tmpi;
  }
  nComponents++;
  return lastComponent++;
}

// ci = config instance name (set to _instname by default in createInstances)
int cComponentManager::addComponent(const char *_instname, const char *_type, const char *_ci, int _threadId)
{
  SMILE_DBG(3,"addComponent: instname='%s' type='%s'",_instname,_type);
  int t = findComponentType(_type);
  if (t >= 0) {
    cSmileComponent *c = createComponent(_instname,t);
    if (c==NULL) COMP_ERR("failed creating component '%s' (type: '%s')",_instname,_type);
    if (_ci != NULL) c->setConfigInstanceName(_ci);
    return registerComponentInstance(c, _type, _threadId);
  } else {
    SMILE_ERR(1,"cannot add component (instname='%s' type='%s'): unknown component type!!",_instname,_type);
  }

  return t;
}

cSmileComponent * cComponentManager::createComponent(const char *_instname, const char *_type)
{
  int t = findComponentType(_type);
  if (t >= 0) {
    return createComponent(_instname,t);
  } else {
    SMILE_ERR(1,"cannot create component (instname='%s' type='%s'): unknown component type!!",_instname,_type);
    return NULL;
  }
}

// n is index of component type in compTs
cSmileComponent * cComponentManager::createComponent(const char *_instname, int n)
{
  if ((n>=0)&&(n<nCompTs)) {
    cSmileComponent *c = (compTs[n].create)(_instname);
    if (c==NULL) OUT_OF_MEMORY;
    c->setComponentEnvironment(this, -1, NULL); // set component manager reference and the component ID, used by componentManager
    return c;
  } else {
    SMILE_ERR(1,"cannot create component of type (index=%i): index is out of range (0 - %i)!",n,nCompTs);
  }
  return NULL;
}

int cComponentManager::registerComponentInstance(cSmileComponent * _component, const char *_typename, int _threadId)
{
  if (_component == NULL) {
    SMILE_ERR(1,"registerComponentInstance: cannot register NULL component instance!");
    return -1;
  }
  int id = getNextComponentId();
  if (id >= 0) {
    _component->setComponentEnvironment(this, id, NULL);
    //_component->setId(id);
    component[id] = _component;
    if (_typename != NULL)
      componentInstTs[id] = strdup(_typename);
    else
      componentInstTs[id] = NULL;
    componentThreadId[id] = _threadId;
  } else {
    SMILE_ERR(1,"registerComponentInstance: could not get next component id, return value == %i!",id);
  }
  return id;
}

void cComponentManager::unregisterComponentInstance(int id, int noDM)  // unregister and destroy component object
{
  // TODO:::: the component would have to unregister it's reader/writer etc...
  if ((id>=0)&&(id < lastComponent)&&(id < nComponentsAlloc)) {
    if (component[id] != NULL) {
      if ((noDM)&&(!strcmp(component[id]->getTypeName(),COMPONENT_NAME_CDATAMEMORY))) {
        return;
      } else {
        delete component[id];
        if (componentInstTs[id] != NULL) {
          free(componentInstTs[id]);
          componentInstTs[id] = NULL;
          componentThreadId[id] = 0;  // TODO: stop thread ?????
        }
        component[id] = NULL;
        nComponents--;
        if (id == lastComponent) lastComponent--;
      }
    }
  }
}

void cComponentManager::resetInstances()
{
  int i;
  // TODO: abort processing , stop threads...etc.??
  int mylastComponent = lastComponent;
  for (i=0; i<mylastComponent; i++) {
    unregisterComponentInstance(i,1);  // all BUT dataMemories...
  }

  mylastComponent = lastComponent;
  for (i=0; i<mylastComponent; i++) {
    unregisterComponentInstance(i); // now free the dataMemories
  }
  nComponents = 0;
  lastComponent = 0; // ???
  ready=0;    // flag that indicates if all components are set up and ready...
  isConfigured=0;
  isFinalised=0;
  EOI=0;
}

int cComponentManager::findComponentInstance(const char *_compname) const
{
  int i;
  if (_compname == NULL) return -1;
  for (i=0; i<lastComponent; i++) {
    if ((component[i] != NULL)&&(!strcmp(_compname,component[i]->getInstName()))) { return i; }
  }
  return -1;
}

cSmileComponent * cComponentManager::getComponentInstance(int n)
{
  if ((n>=0)&&(n<nComponents)) return component[n];
  else return NULL;
}

const char * cComponentManager::getComponentInstanceType(int n)
{
  if ((n>=0)&&(n<nComponents)) return componentInstTs[n];
  else return NULL;
}

cSmileComponent * cComponentManager::getComponentInstance(const char *_compname)
{
  return getComponentInstance(findComponentInstance(_compname));
}

const char * cComponentManager::getComponentInstanceType(const char *_compname)
{
  return getComponentInstanceType(findComponentInstance(_compname));
}

// send inter component messages directly to component (string version, takes recepient component name as first argument, sending to multiple components is possible, if they are separated via a comma ',' in the recepient name argument)
int cComponentManager::sendComponentMessage(const char *_compname, cComponentMessage *_msg)
{
  if (_compname != NULL) {
    char *inp = strdup(_compname);
    char *tmp = strchr(inp,','); // is array of recepients ?
    if (tmp != NULL) {
      char *t = inp;
      tmp = strchr(t,','); // is array of recepients ?
      tmp[0] = 0;
      int ret;
      // first part:
      ret = sendComponentMessage(findComponentInstance(t),_msg);
      // second part:
      tmp++;
      ret += sendComponentMessage(tmp, _msg);
      free(inp);
      return ret;
    } else {
      free(inp);
      return sendComponentMessage(findComponentInstance(_compname),_msg);
    }
  }
  return 0;
}

// send inter component messages directly to component:
int cComponentManager::sendComponentMessage(int compid, cComponentMessage *_msg)
{
  cSmileComponent *c = getComponentInstance(compid);
  int ret = 0;
  if (c!=NULL) {
    if (_msg != NULL) {
      // assign timestamp
      _msg->smileTime = getSmileTime();
      // assign unique message id from message counter:
      smileMutexLock(messageMtx);
      _msg->msgid = messageCounter++; // MUTEX!!
      smileMutexUnlock(messageMtx);
    }
    ret = c->receiveComponentMessage(_msg);
  }
  return ret;
}

double cComponentManager::getSmileTime()
{
  struct timeval curTime;
  gettimeofday( &curTime, NULL );
  return ( (double)(curTime.tv_sec - startTime.tv_sec) + (double)(curTime.tv_usec - startTime.tv_usec)/1000000.0 );
}

int cComponentManager::tick(int threadId, long long tickNr)
{
  if (!ready) return 0;
  int i;
  int nRun = 0; int nRunnable = 0;
  for (i=0; i<=lastComponent; i++) {
    if (component[i] != NULL) {
      if (((threadId == -1)||(threadId == componentThreadId[i]))&&(componentThreadId[i]!=-2)) {
        nRunnable++;
        SMILE_DBG(5,"~~~~> 'ticking' component '%s' (idx %i)",component[i]->getInstName(),i);
        if (component[i]->tick(tickNr,EOI)) {
          nRun++;
          SMILE_DBG(5,"%s.tick() executed successfully!",component[i]->getInstName());
        }
      }
    }
  }
  if (nRun < nRunnable) SMILE_MSG(7,"not all components were run during tick %i ! (%i<%i)",tickNr,nRun,nRunnable);
  return nRun;
}

// single thread tick loop
long long cComponentManager::runSingleThreaded(long long maxtick)
{
  int nRun;
  if (!ready) return 0;
  SMILE_MSG(2,"starting single thread processing loop");
  // TODO: external abort mechanism... (Ctrl+C, Message, etc.)
  long long tickNr = -1;
  do {
    tickNr++;
    SMILE_DBG(4,"<------- TICK # %i ---------->",tickNr);
    nRun = tick(-1, tickNr);
    if ((maxtick != -1)&&(tickNr >= maxtick)) nRun = 0;
    smileMutexLock(abortMtx);
    if (abortRequest) nRun = 0;
    smileMutexUnlock(abortMtx);
    if (nRun > 0) userOnTick(tickNr,EOI);
  } while(nRun > 0);
  if ((tickNr < maxtick)||(maxtick==-1)) {
    EOI = 1; // set EOI and run another tick loop
    do {
      //printf("EOI tick %i\n",tickNr);
      tickNr++;
      SMILE_DBG(4,"<------- TICK # %i ---------->",tickNr);
      nRun = tick(-1, tickNr);
      if ((maxtick != -1)&&(tickNr >= maxtick)) nRun = 0;
      // ???
      smileMutexLock(abortMtx);
      if (abortRequest) nRun = 0;
      smileMutexUnlock(abortMtx);
      if (nRun > 0) userOnTick(tickNr,EOI);
    } while(nRun > 0);
  }
  SMILE_MSG(2,"Processing finished! System ran for %i ticks.",tickNr);
  return tickNr;
}


SMILE_THREAD_RETVAL threadRunner(void *_data)
{
  sThreadData *data = (sThreadData*)_data;
  if ((data != NULL)&&(data->obj!=NULL)) {
    data->obj->tickLoopA(data->maxtick, data->threadId);
    // wait for all threads to be in this state....
    data->obj->waitForAllThreads(data->threadId);
    // post EOI processing
    data->obj->tickLoopA(data->maxtick, data->threadId);
  }
  SMILE_THREAD_RET;
}

void cComponentManager::waitForAllThreads(int threadID)
{
  smileMutexLock(waitEndMtx);
  waitEndCnt++; SMILE_DBG(4,"thread %i entered waiting state.. %i threads of %i are now waiting\n",threadID,waitEndCnt,nThreads);
  if (waitEndCnt == nThreads) {
    EOI = 1; nActive = nThreads;
    smileCondBroadcast(waitEndCond);
  } else {
    // wait;
    smileCondWaitWMtx(waitEndCond,waitEndMtx);
  }
  smileMutexUnlock(waitEndMtx);
}

// multi thread tick loop (tick loop for one of many threads)
long long cComponentManager::tickLoopA(long long maxtick, int threadId)
{
  int nRun;
  long long tickNr = -1;
  int nRun0cnt = 0;

  SMILE_MSG(2,"starting processing loop of thread %i",threadId);

  /*
  smileMutexLock(syncCondMtx);
  // TODO: BUG, if nActive == 1, because other threads have not yet been started!!! (maybe initialise nActive with nThreads!?)
  nActive++;
  smileMutexUnlock(syncCondMtx);
  */

  do {
    tickNr++;
    SMILE_DBG(4,"<------- TICK # %i (thread %i) ---------->",tickNr,threadId);
    nRun = tick(threadId,tickNr);
    //    smileYield();
    SMILE_DBG(4,"nRun = %i (thread %i)",nRun,threadId);
    smileMutexLock(syncCondMtx);
    //    fprintf(stderr,"mutlock...%i\n",threadId);
    if (nRun==0) {
      // if not all waiting... wait!
      //          fprintf(stderr,"wc? %i nW %i nA %i\n",threadId,nWaiting,nActive); fflush(stderr);

      // TODO: BUG, if nActive == 1, because other threads have not yet been started!!! (maybe initialise nActive with nThreads!?)
      if (nWaiting < nActive-1) {
        nWaiting++;
        //          fprintf(stderr,"entering wait cond %i nW %i nA %i\n",threadId,nWaiting,nActive); fflush(stderr);
        smileCondWaitWMtx(syncCond,syncCondMtx);
        //          fprintf(stderr,"exiting wait cond %i\n",threadId); fflush(stderr);
        nWaiting--;
        nRun=1;
      } //else  //all threads seem to have failed.... nRun=0, this will exit the first loop
      else {
        nRun0cnt++;
        if (nRun0cnt <= 1) { nRun = 1; smileYield(); }
      }
    } else {
      //      smileMutexLock(syncCondMtx);
      userOnTick(tickNr,EOI,threadId);
      nRun0cnt = 0;
    }
    if ((maxtick != -1)&&(tickNr >= maxtick)) nRun = 0;
    if (nRun == 0) nActive--;
    smileCondBroadcastRaw(syncCond);
    smileMutexUnlock(syncCondMtx);
    smileMutexLock(abortMtx);
    if (abortRequest) nRun = 0;
    smileMutexUnlock(abortMtx);
  } while(nRun > 0);

  //  smileMutexLock(syncCondMtx);
  // we must signal, if we exit, in order to wake up other threads, to allow them to check , if they are finished too
  //  smileCondBroadcastRaw(syncCond);
  //  smileMutexUnlock(syncCondMtx);

  SMILE_MSG(2,"leaving processing loop of thread %i",threadId);
  // first part... now enter EOI state, however wait for other threads...???

  return tickNr;
}

// multi thread tick loop (tick loop for one of many threads)
//long long cComponentManager::tickLoopB(long long maxtick, int threadId)//
//{
//TODO... post EOI processing... (not needed... we will try to use tickLoopA again..)

//  return 0;
//}

//
// !!! THIS function should be always preferred, since it determines single/multi thread from config !!!
//
// multi threaded run: create threads for multiple tick loops and control/synchronize them...
long long cComponentManager::runMultiThreaded(long long maxtick)
{
  if (!ready) return 0;
  int i;

  if (nThreads == 1) {
    return runSingleThreaded(maxtick);
  } else {
    if (nThreads == 0) {
      int j=0;
      for (i=0; i<lastComponent; i++) {
        if (componentThreadId[i] != -2) {
          componentThreadId[i] = j++;
        }
      }
      nThreads = j;

    }
    SMILE_MSG(2,"starting mutli-thread processing with %i threads",nThreads);
    // create thread handles and data structures
    sThreadData *threadData = (sThreadData*)malloc(sizeof(sThreadData) * nThreads);
    smileThread *threadHandles = (smileThread *)malloc(sizeof(smileThread) * nThreads);
    smileMutexCreate(syncCondMtx);
    smileCondCreate(syncCond);
    smileCondCreate(waitEndCond);

    nActive = nThreads;
    waitEndCnt = 0;
    smileMutexCreate(waitEndMtx);

    // create all the threads....
    for (i=0; i<nThreads; i++) {
      threadData[i].obj = this;
      threadData[i].maxtick = maxtick;
      threadData[i].threadId = i;
      if (!smileThreadCreate(threadHandles[i], threadRunner, &(threadData[i]))) {
        //      if (!((long)(threadHandles[i] = (HANDLE)_beginthread(threadRunner,0,&(threadData[i]))) != -1)) {
        SMILE_ERR(1,"error creating thread with threadId %i!!",i);
        smileMutexLock(syncCondMtx);
        nActive--;
        smileMutexUnlock(syncCondMtx);
      }
    }

    // wait for all threads to finish
    for (i=0; i<nThreads; i++) {
      smileThreadJoin(threadHandles[i]);
    }

    smileMutexDestroy(messageMtx);
    smileMutexDestroy(waitEndMtx);
    smileMutexDestroy(syncCondMtx);
    smileCondDestroy(syncCond);
    smileCondDestroy(waitEndCond);

    // destroy all threads and thread data:
    if (threadData != NULL) free(threadData);
    if (threadHandles != NULL) free(threadHandles);
  }
  return 1; // TODO: tickNr??
}


cComponentManager::~cComponentManager()
{
  int i;

  resetInstances();

  for (i=0; i<lastComponent; i++) {
    //    unregisterComponentInstance(i);
    if ((componentInstTs!=NULL)&&(componentInstTs[i] != NULL)) free(componentInstTs[i]);
  }
  if (componentThreadId != NULL) free(componentThreadId);
  if (component != NULL) free(component);
  if (compTs != NULL) free(compTs);
  if (componentInstTs != NULL) free(componentInstTs);
  smileMutexDestroy(abortMtx);

#ifdef SMILE_SUPPORT_PLUGINS   // NOTE: the config Manager must be free before
  //close dynlibs of plugins:
  if ((handlelist != NULL)&&(nPluginHandles>0)) {
    for (i=0; i<nPluginHandles; i++) {
#ifdef __WINDOWS
      FreeLibrary(handlelist[i]);
#else
      dlclose(handlelist[i]);
#endif
    }
    free(handlelist);
  }
  if (regFnlist != NULL) free(regFnlist);
#endif

}
