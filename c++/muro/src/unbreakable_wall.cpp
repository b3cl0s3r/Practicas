#include "../include/unbreakable_wall.hpp"


unbreakable_wall::unbreakable_wall(int w, int h){
  generar_filas(row_t(w));

  unsigned t0, t1;
  t0=clock();
  generar_pared(wall_t(w, h));
  t1=clock();
  time = (double(t1-t0)/CLOCKS_PER_SEC);
  std::cout << time;
}


void unbreakable_wall::generar_pared(wall_t wall){

  for(int i=0; i<allrows.size(); i++){

    if(wall.get_height()==wall.get_current_height()){
      validwalls.push_back(wall);
      return;
    }
    else if((wall.get_height()>wall.get_current_height())){

      wall.push_row(allrows[i]);

      if(wall.get_current_height()==1){
        generar_pared(wall);
      }
      else{
        row_t lastrow=  wall.get_row(wall.get_current_height()-1);
        row_t penultime = wall.get_row(wall.get_current_height()-2);

        if(wall.compare_rows(penultime, lastrow)){
          generar_pared(wall);
        }
      }
    }

    wall.pop_row();
  }
}


void unbreakable_wall::generar_filas(row_t row){

  if(row.maxwidth() == row.current_sz()){
    allrows.push_back(row);
  }
  else if(row.maxwidth() > row.current_sz()){

    row.push_block(block_t(2));
    generar_filas(row);

    row.pop_block();
    row.push_block(block_t(3));
    generar_filas(row);
  }
}

void unbreakable_wall::print_validwalls(void){
  if(validwalls.size()==0){
      std::cout << bold << red << "\n[!] No existe ninguna combinación de filas válida para generar un muro. \n" << reset;
  }
  else{
    std::cout << bold << white << "***  " << validwalls.size() << " MUROS VÁLIDOS  *** \n\n" << reset;

    for(int i=0; i<validwalls.size(); i++)
      std::cout << "Muro " << i+1 << ": \n\n" << validwalls[i] << "\n";

    std::cout << yellow << "\n\nTiempo de ejecución: " << white << time << "\n\n";


  }
}

void unbreakable_wall::print_allrows(void){
  if(allrows.size()==0){
    std::cout << bold << red << "\n[!] No existen filas \n" << reset;
  }
  else{
    std::cout << bold << white << "\n***  " << allrows.size() << " POSIBLES FILAS  *** \n\n" << reset;

    for(int i=0; i<allrows.size(); i++)
      std::cout << allrows[i] << "\n\n";

    std::cout << "\n";
  }
}
