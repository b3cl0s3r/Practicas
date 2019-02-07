#include <vector>
#include <ctime>
#include "../include/termcolor.hpp"
#include "../include/wall_t.hpp"
#include "../include/row_t.hpp"
#include "../include/block_t.hpp"

class unbreakable_wall
{
    private:
        std::vector<wall_t> validwalls;
        std::vector<row_t> allrows;
        double time;

    public:
        unbreakable_wall(int w, int h);

        ~unbreakable_wall(void){}

        void print_validwalls(void);
        void print_allrows(void);

    private:

        void generar_filas(row_t row);
        void generar_pared(wall_t wall);
};
