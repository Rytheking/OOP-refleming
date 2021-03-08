#pragma once

#include <string>
#include <memory>


namespace france {

class Country {
    public: static const std::string DEFAULT_CONTINENT;  // 1.
    private: float m_GDP; // 1 per instance
    private: const std::string m_continent; // 1 per instance
    
    public: Country(float GDP);
    public: Country(float GDP, const std::string &continent);

    public: float GDP() const;
    public: void GDP(float value);
    public: const std::string& continent() const;
    public: virtual ~Country();
};

typedef std::shared_ptr < Country > CountryPtr;


}