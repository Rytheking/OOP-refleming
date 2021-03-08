#include "moon.h"
#include <stdexcept>

namespace moon
{

    Moon::Moon(int size, std::string color, int phase)
    {
        m_size = size;
        m_color = color;
        m_phase = phase;
    }
    bool Moon::isNewMoon()
    {
        return m_phase == 0;
    }
    void Moon::cycle()
    {
        m_phase = (m_phase + 1) % 4;
    }
    int Moon::phase()
    {
        return m_phase;
    }
    int Moon::size()
    {
        return m_size;
    }
    std::string Moon::color()
    {
        return m_color;
    }
    void Moon::color(std::string value)
    {
        if (!(value == "sivler" || value == "white"))
        {
            throw std::invalid_argument("invalid color");
        }
        m_color = value;
    }

} // namespace moon