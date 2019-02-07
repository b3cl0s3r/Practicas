#include "../include/row_t.hpp"


void row_t::push_block(block_t block){
  currentsz_ += block.get_sz();
  row_.push_back(block);
}

void row_t::write(std::ostream& os) const
{
  for(int i=0; i<row_.size(); i++){

    if(i%2==0){
      os << white << bold << on_green << row_[i] << reset;
    } else{
      os << white << bold << on_yellow << row_[i] << reset;
    }

  }
}

int row_t::current_sz(void){
  return currentsz_;
}

int row_t::maxwidth(void){
  return maxwidth_;
}

int row_t::vector_sz(void){
  return row_.size();
}

void row_t::pop_block(void){
    currentsz_-=row_[row_.size()-1].get_sz();
    row_.pop_back();
}

block_t row_t::get_block(int pos){
    return row_[pos];
}

std::ostream& operator<<(std::ostream& os, const row_t& a)
{
    a.write(os);
    return os;
}
