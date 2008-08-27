#ifndef GEOMETRY_HCALTOWERALGO_HCALHARDCODEGEOMETRYLOADER_H
#define GEOMETRY_HCALTOWERALGO_HCALHARDCODEGEOMETRYLOADER_H 1

#include "Geometry/CaloGeometry/interface/CaloVGeometryLoader.h"
#include "Geometry/CaloTopology/interface/HcalTopology.h"

class CaloCellGeometry;
class HcalDetId;

/** \class HcalHardcodeGeometryLoader
 *
 *
 * \note The HE geometry is not currently correct.  The z positions must be corrected.
 *   
 * $Date: 2008/04/21 22:19:36 $
 * $Revision: 1.6 $
 * \author R. Wilkinson - Caltech
*/
class HcalHardcodeGeometryLoader 
{
   public:

      typedef CaloSubdetectorGeometry* ReturnType ;

      HcalHardcodeGeometryLoader();
      explicit HcalHardcodeGeometryLoader(const HcalTopology& ht);
      virtual ~HcalHardcodeGeometryLoader() { delete theTopology ; }
  
      ReturnType load(DetId::Detector det, int subdet);
  /// Load all of HCAL
      ReturnType load();
  
   private:
      void init();
      /// helper functions to make all the ids and cells, and put them into the
      /// vectors and mpas passed in.

      void fill( HcalSubdetector  subdet, 
		 int              firstEtaRing, 
		 int              lastEtaRing,
		 ReturnType       cg              );
  
      CaloCellGeometry* makeCell( const HcalDetId& detId,
				  ReturnType       geom   ) const;
  
      HcalTopology*       theTopology;
      const HcalTopology* extTopology;
  
      double theBarrelRadius;
      double theOuterRadius;
      double theHEZPos[4];
      double theHFZPos[2];
  
      double theHBThickness;
      double theHB15aThickness,theHB15bThickness;
      double theHB16aThickness,theHB16bThickness;
      double theHFThickness;
      double theHOThickness;
};

#endif
