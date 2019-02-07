#include <vector>
#include "../include/wall_t.hpp"
#include "../include/row_t.hpp"
#include "../include/block_t.hpp"
#include "../include/termcolor.hpp"
#include "../include/unbreakable_wall.hpp"

using namespace termcolor;

int main (void){

  int x, y;

  std::cout << bold << yellow << "Ancho del muro: " << white;
  std::cin >> x;
  std::cout << yellow << "Alto del muro: " << white;
  std::cin >> y;

  std::cout << reset;

  unbreakable_wall test(x, y);

  test.print_allrows();
  test.print_validwalls();
}
