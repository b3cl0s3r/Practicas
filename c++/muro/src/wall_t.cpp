#include "../include/wall_t.hpp"

void wall_t::write(std::ostream& os) const
{
  for(int i=0; i<rows_.size(); i++){
    os << rows_[i] << "\n";
  }
}

void wall_t::push_row(row_t row){
  rows_.push_back(row);
}

void wall_t::pop_row(void){
  rows_.pop_back();
}

row_t wall_t::get_row(int pos){
  return rows_[pos];
}

int wall_t::get_height(void){
  return height_;
}

int wall_t::get_current_height(void){
  return rows_.size();
}


bool wall_t::compare_rows(row_t a, row_t b){

  int atotal=0, btotal=0;
  int i = 0, j = 0;

  std::vector<int> va_sumas;
  std::vector<int> vb_sumas;

  for(int i=0; i<a.vector_sz(); i++){
      atotal += a.get_block(i).get_sz();
      va_sumas.push_back(atotal);
  }

  for(int i=0; i<b.vector_sz(); i++){
      btotal += b.get_block(i).get_sz();
      vb_sumas.push_back(btotal);
  }

  for(int i=0; i<va_sumas.size()-1; i++){
    for(int j=0; j<vb_sumas.size()-1; j++){
      if(va_sumas[i]==vb_sumas[j]){
        return false;
      }
    }
  }

  return true;
}


std::ostream& operator<<(std::ostream& os, const wall_t& a)
{
    a.write(os);
    return os;
}


///////////////////////////////////////////

/*
  for (int i=0; i<a.vector_sz(); i++){

    if((btotal==atotal)&&(i<a.vector_sz()-1)&&(atotal!=0)){
      return false;
    }

    atotal += a.get_block(i).get_sz();

    if((btotal==atotal)&&(i<a.vector_sz()-1)){
      return false;
    }

    btotal += b.get_block(i).get_sz();

    if((btotal==atotal)&&(i<a.vector_sz()-1)){
      return false;
    }
  }
  if(a.get_block(a.vector_sz()-1).get_sz()==b.get_block(b.vector_sz()-1).get_sz()){
    return false;
  }*/
