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


/*  openSMILE component:

number of segments based on delta thresholding

*/


#ifndef __CFUNCTIONALSEGMENTS_HPP
#define __CFUNCTIONALSEGMENTS_HPP

#include <smileCommon.hpp>
#include <dataMemory.hpp>
#include <functionalComponent.hpp>

#define COMPONENT_DESCRIPTION_CFUNCTIONALSEGMENTS "number of segments based on delta thresholding"
#define COMPONENT_NAME_CFUNCTIONALSEGMENTS "cFunctionalSegments"

class cFunctionalSegments : public cFunctionalComponent {
  private:
    long maxNumSeg;
	FLOAT_DMEM rangeRelThreshold;
	//int overlapFlag;

  protected:
    SMILECOMPONENT_STATIC_DECL_PR
    virtual void fetchConfig();

  public:
    SMILECOMPONENT_STATIC_DECL
    
    cFunctionalSegments(const char *_name);
    // inputs: sorted and unsorted array of values, out: pointer to space in output array, You may not return MORE than Nout elements, please return as return value the number of actually computed elements (usually Nout)
    virtual long process(FLOAT_DMEM *in, FLOAT_DMEM *inSorted, FLOAT_DMEM *out, long Nin, long Nout);
    //virtual long process(INT_DMEM *in, INT_DMEM *inSorted, INT_DMEM *out, long Nin, long Nout);

    virtual long getNoutputValues() { return nEnab; }
    virtual int getRequireSorted() { return 0; }

    virtual ~cFunctionalSegments();
};




#endif // __CFUNCTIONALSEGMENTS_HPP
