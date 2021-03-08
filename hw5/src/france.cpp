#include "france.h"

namespace france
{
    France::France(std::string govtype, std::string head, int population, int year)
    {
        m_govtype=govtype;
        m_head=head;
        m_population=population;
        m_year=year;
    }

    void France::newYear()
    {
        m_year++;
        m_population*=1.14;
    }
    //getters
    std::string France::govType()
    {
        return m_govtype;
    }
    std::string France::head()
    {
        return m_head;
    }
    int France::population()
    {
        return m_population;
    }
    int France::year()
    {
        return m_year;
    }

    //setters
    void France::govType(std::string value)
    {
        m_govtype=value;
    }
    void France::head(std::string value)
    {
        m_head=value;
    }
    void France::population(int value)
    {
        m_population=value;
    }
    void France::year(int value)
    {
        m_year=value;
    }
}