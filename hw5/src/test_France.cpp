#include "France.h"
#include "gtest/gtest.h"

using namespace std;
using namespace france;

TEST(France, Constructor)
{
  float GDP = 9009090;
  std::string continent ="antartica";
  string govType="Monarchy";
  string head="Charlemange";
  int population=1000;
  int year=900;
  France France(GDP, continent, govType, head, population, year);
  ASSERT_EQ(France.GDP(), GDP);
  ASSERT_EQ(France.continent(), continent);
  ASSERT_EQ(France.govType(), govType);
  ASSERT_EQ(France.head(), head);
  ASSERT_EQ(France.population(), population);
  ASSERT_EQ(France.year(), year);
  France.newYear();
  ASSERT_EQ(France.year(), year+1);
  ASSERT_EQ(France.population(), (population*1.14));
}

TEST(France, DefaultConstructor)
{
  float GDP = 13000000;
  std::string continent ="Europe";
  string govType="Facist Dictatorship";
  string head="Marie LaPen";
  int population=60000000;
  int year=2030;

  France France;

  ASSERT_EQ(France.GDP(), GDP);
  ASSERT_EQ(France.continent(), continent);
  ASSERT_EQ(France.govType(), govType);
  ASSERT_EQ(France.head(), head);
  ASSERT_EQ(France.population(), population);
  ASSERT_EQ(France.year(), year);
}

TEST(France, FranceAsCountry) {
      std::shared_ptr < Country > pCount (new France());

      std::shared_ptr < Country > qCount (new Country(13333333));

      ASSERT_EQ(pCount->continent(), Country::DEFAULT_CONTINENT);
      ASSERT_EQ(qCount->continent(), Country::DEFAULT_CONTINENT);
}

TEST(France, FranceAsCountryBad1) {
      Country *pCount=new France();
      Country *qCount=new Country(14444444);

      ASSERT_EQ(pCount->continent(), Country::DEFAULT_CONTINENT);
      ASSERT_EQ(qCount->continent(), Country::DEFAULT_CONTINENT);
}

TEST(France, FranceAsCountryBad2) {
      Country *pCount=new France();
      Country *qCount=new Country(166666666);

      ASSERT_EQ(pCount->continent(), Country::DEFAULT_CONTINENT);
      ASSERT_EQ(qCount->continent(), Country::DEFAULT_CONTINENT);

      delete pCount; // only cleans Countryness!!!! 
      delete qCount;
}
int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
