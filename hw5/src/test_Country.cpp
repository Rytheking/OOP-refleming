#include "Country.h"
#include "gtest/gtest.h"

using namespace std;
using namespace france;

TEST(Country, Constructor) {
      float GDP = 314000000000;
      string continent("europe");
      Country Country(GDP,continent);
      ASSERT_EQ(Country.GDP(),GDP);
      ASSERT_EQ(Country.continent(),continent);
      float newGDP = 130000;
      Country.GDP(newGDP);
      ASSERT_EQ(Country.GDP(),newGDP);
}

TEST(Country, Constness) {
      float GDP = 999999;
      string continent("africa");

      const Country Country(GDP,continent);
      ASSERT_EQ(Country.GDP(),GDP);
      ASSERT_EQ(Country.continent(),continent);
}

int main(int argc, char** argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}