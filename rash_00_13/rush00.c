#include <unistd.h>

void ft_putchar(char c);
void print_char_n_times(int nn, char bb);
void print_first_row(int lengh);
void print_middle_row(int lengh);
void print_last_row(int lengh, int deepler);
void rush(int i, int j);

void    print_char_n_times(int nn, char bb)
{
    while(nn > 0)
    {
        ft_putchar(bb);
        nn--;
    }
}

void    print_first_row(int lengh)
{
    ft_putchar('o');
    if (lengh == 2)
        ft_putchar('o');
    else if (lengh >= 3)
    {
        print_char_n_times(lengh - 2, '-');
        ft_putchar('o');
    }
    ft_putchar('\n');
}

void    print_middle_row(int lengh)
{
    ft_putchar('|');
    if (lengh == 2)
        ft_putchar('|');
    else if (lengh >= 3)
    {
        print_char_n_times(lengh - 2, ' ');
        ft_putchar('|');
    }
    ft_putchar('\n');
}

void    print_last_row(int lengh, int deepler)
{
    if (deepler >= 3)
    {
        ft_putchar('o');
        if (lengh == 2)
            ft_putchar('o');
        else if (lengh >= 3)
        {
            print_char_n_times(lengh - 2, '-');
            ft_putchar('o');
        }
        ft_putchar('\n');
    }
}

void    rush(int i, int j)
{
    int kk;

    if ((i * j <= 0) || (i <= 0) || (i > 2147483647) || (j > 2147483647))
    {
        write(1, "error ! expected input", 23);
    }
    else
    {
        kk = j;
        print_first_row(i);
        if ( j == 2)
            print_middle_row(i);
        else if (j >= 3)
        {
            while(kk-- > 2)
            {
                print_middle_row(i);
            }
            print_last_row(i, j);
        }
    }
}