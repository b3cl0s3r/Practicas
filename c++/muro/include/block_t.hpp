#pragma once

#include <iostream>
#include "termcolor.hpp"

using namespace termcolor;

class block_t
{
    private:
      int sz_;

    public:
      block_t();

      block_t(int sz):
      sz_(sz) {}

      ~block_t(void) {}

      void write(std::ostream& os) const;
      int get_sz(void);
};

std::ostream& operator<<(std::ostream& os, const block_t& a);
