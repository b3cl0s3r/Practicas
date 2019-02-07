#pragma once

#include <iostream>
#include <vector>
#include "../include/block_t.hpp"


class row_t
{
    private:
        int maxwidth_;
        int currentsz_;
        std::vector<block_t> row_;

    public:
        row_t(int w):
        maxwidth_(w),
        currentsz_(0){}

        ~row_t(void) {}

        void push_block(block_t block);
        void pop_block(void);

        int current_sz(void);
        int vector_sz(void);
        int maxwidth(void);

        block_t get_block(int pos);

        void write(std::ostream& os) const;
};

std::ostream& operator<<(std::ostream& os, const row_t& a);
