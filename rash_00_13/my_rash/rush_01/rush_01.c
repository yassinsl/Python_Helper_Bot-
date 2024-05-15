void ft_putchar(char c);
void  print_slash(char c, char k)
{
    static int i = 1;

    if(i > 2)
		i = 0;
	char slash = (i == 1) ? c : k;
	ft_putchar(slash);
	i++; 
}
void rush (int x, int y)
{
	int  i = 1, j;

	while(i <= y)
		{
			j = 1;
			while(j <= x)
			{
			if(i == 1 || i == y)
				{
					if (j == 1 || j == x)
						print_slash('/', '\\');
					else
						ft_putchar('*');
				}

			else if(j == 1 || j == x)
				ft_putchar('*');
			else
				ft_putchar(' ');
			++j;
			}
			ft_putchar('\n');
		i++;
		}
}