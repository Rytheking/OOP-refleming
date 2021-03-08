#include "france.h"
#include "gtest/gtest.h"

using namespace std;
using namespace france;

TEST(France, Constructor)
{
  string govType="Monarchy";
  string head="Charlemange";
  int population=1000;
  int year=900;
  France France(govType, head, population, year);
  ASSERT_EQ(France.govType(), govType);
  ASSERT_EQ(France.head(), head);
  ASSERT_EQ(France.population(), population);
  ASSERT_EQ(France.year(), year);
  France.newYear();
  ASSERT_EQ(France.year(), year+1);
  ASSERT_EQ(France.population(), (population*1.14));
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
