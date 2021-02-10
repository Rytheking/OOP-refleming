#include <string>

namespace france
{

    class France
    {
        private: std::string m_govtype;
        private: std::string m_head;
        private: int m_population;
        private: int m_year;

        public: France(std::string govtype, std::string head, int population, int year);

        //function
        public: void newYear();

        //getters
        public: std::string govType();
        public: std::string head();
        public: int population();
        public: int year();

        //setters
        public: void govType(std::string value);
        public: void head(std::string value);
        public: void population(int value);
        public: void year(int value);



    };
} // namespace france