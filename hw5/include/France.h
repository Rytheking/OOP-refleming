#pragma once

#include <string>
#include "Country.h"

namespace france
{

    class France: public Country
    {
        private: std::string m_govtype;
        private: std::string m_head;
        private: int m_population;
        private: int m_year;

        public: France();

        public: France(float GDP,const std::string continent,  std::string govtype, std::string head, int population, int year);

        public : virtual ~France();
        //function
        public: void newYear();

        //getters
        public: std::string govType() const;
        public: std::string head() const;
        public: int population() const;
        public: int year() const;

        //setters
        public: void govType(std::string value);
        public: void head(std::string value);
        public: void population(int value);
        public: void year(int value);



    };

    typedef std::shared_ptr < France > FrancePtr;
} // namespace france