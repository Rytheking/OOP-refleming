#pragma once
#include <string>

namespace moon
{
    class Moon
    {
        private: int m_size;
        private: int m_phase;
        private: std::string m_color;

        public: Moon(int size, std::string color, int phase = 0);
        
        public: bool isNewMoon();
        public: void cycle();
        public: int phase();
        public: int size();
        public: std::string color();
        public: void color(std::string value);

            

        
    };
} // namespace moon