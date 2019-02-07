#include "../include/block_t.hpp"


int block_t::get_sz(void){
  return sz_;
}


void block_t::write(std::ostream& os) const
{
  if (sz_ == 2){
    os << "xx";
    //os << bold << white << on_green << "xx" << reset;
  }
  else if (sz_ == 3){
    os << "xxx";
    //os << bold << white << on_yellow << "xxx" << reset;
  }
}


std::ostream& operator<<(std::ostream& os, const block_t& a)
{
    a.write(os);
    return os;
}
