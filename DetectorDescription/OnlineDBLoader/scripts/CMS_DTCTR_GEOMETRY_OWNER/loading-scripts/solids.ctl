LOAD DATA
INFILE './data/SOLIDS'
BADFILE './data/SOLIDS.bad'
DISCARDFILE './data/SOLIDS.dsc'
INSERT INTO TABLE CMS_DTCTR_GEOMETRY_OWNER.SOLIDS
FIELDS TERMINATED by ","
(
 NAME CHAR,
 SOL_TYPE CHAR
)
 
