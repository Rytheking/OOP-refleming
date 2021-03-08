#include "France.h"

#include <iostream>

namespace france
{
    France::France()
    : Country(13000000)
    {
        m_govtype = "Facist Dictatorship";
        m_head = "Marie LaPen";
        m_population = 60000000;
        m_year = 2030;
        std::cout << "France@" << (void *)this << " constructed." << std::endl;
    }

    France::France(std::string continent, float GDP, std::string govtype, std::string head, int population, int year)
    :Country(GDP, continent)
    {
        m_govtype = govtype;
        m_head = head;
        m_population = population;
        m_year = year;
        std::cout << "France@" << (void *)this << " constructed." << std::endl;
    }

    France::~France()
    {
        std::cout << "France@" << (void *)this << " destructed." << std::endl;
    }

    void France::newYear()
    {
        m_year++;
        m_population *= 1.14;
    }
    //getters
    std::string France::govType() const
    {
        return m_govtype;
    }
    std::string France::head() const
    {
        return m_head;
    }
    int France::population() const
    {
        return m_population;
    }
    int France::year() const
    {
        return m_year;
    }

    //setters
    void France::govType(std::string value)
    {
        m_govtype = value;
    }
    void France::head(std::string value)
    {
        m_head = value;
    }
    void France::population(int value)
    {
        m_population = value;
    }
    void France::year(int value)
    {
        m_year = value;
    }
}