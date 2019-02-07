#pragma once

#include <iostream>
#include <vector>
#include "../include/row_t.hpp"
#include "../include/block_t.hpp"


class wall_t
{
    private:
        int width_;
        int height_;
        std::vector<row_t> rows_;

    public:
        wall_t(int w, int h):
        width_(w),
        height_(h){}

        ~wall_t(void) {}

        void write(std::ostream& os) const;

        row_t get_row(int pos);
        void push_row(row_t row);
        void pop_row(void);

        int get_height(void);
        int get_current_height(void);

        bool compare_rows(row_t a, row_t b);
};

std::ostream& operator<<(std::ostream& os, const wall_t& a);
