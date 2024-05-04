-- Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
-- The STATION table is described as follows:

-- STATION

-- -----------------------------------
-- |Field           Type
-- |
-- |ID              NUMBER
-- |CITY            VARCHAR2( 21)
-- |STATE           VARCHAR2(2)
-- |LAT_N           NUMBER
-- |LONG_W          NUMBER
-- -----------------------------------

select DISTINCT CITY from STATION where MOD(id, 2) = 0;