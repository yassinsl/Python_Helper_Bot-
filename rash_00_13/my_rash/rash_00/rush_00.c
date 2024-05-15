void ft_putchar(char c);

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
				char k =(j == 1 || j == x) ? 'o': '-';
				ft_putchar(k);
			}
			else if(j == 1 || j == x)
				ft_putchar('|');
			else
				ft_putchar(' ');
			++j;
			}
			ft_putchar('\n');
		i++;
		}
}