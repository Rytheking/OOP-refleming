#include "country.h"

#include <iostream>

namespace france{
    const std::string Country::DEFAULT_CONTINENT("europe");

    Country::Country(float GDP)
        : m_GDP(GDP), m_continent(DEFAULT_CONTINENT)
    {
        std::cout << "Country@" << (void*) this << " constructed." << std::endl;
    }

    Country::Country(float GDP, const std::string &continent)
        : m_GDP(GDP), m_continent(continent)
    {
        std::cout << "Country@" << (void*) this << " constructed." << std::endl;
    }

    float Country::GDP() const {
        return m_GDP;
    }
    void Country::GDP(float value) { m_GDP = value; }

    const std::string& Country::continent() const { return m_continent; }

    Country::~Country() {
      std::cout << "Country@" << (void*) this << " destructed." << std::endl;
      

    }
}