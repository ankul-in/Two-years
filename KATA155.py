#kata christmastree

#https://www.codewars.com/kata/5a405ba4e1ce0e1d7800012e/train/python
##include <stdio.h>
# int main() {
#    int rows, coef = 1, space, i, j;
#    printf("Enter the number of rows: ");
#    scanf("%d", &rows);
#    for (i = 0; i < rows; i++) {
#       for (space = 1; space <= rows - i; space++)
#          printf("  ");
#       for (j = 0; j <= i; j++) {
#          if (j == 0 || i == 0)
#             coef = 1;
#          else
#             coef = coef * (i - j + 1) / j;
#          printf("%4d", coef);
#       }
#       printf("\n");
#    }
#    return 0;
# }
def custom_christmas_tree(chars, row):
    chars = chars * (row ** 3)
    k = 0
    tree_str = ""
    for i in range(row):
        tree_str += " " * (row - i)
        coef = 1
        for j in range(i + 1):
            tree_str += chars[k] + " "
            k += 1
            coef = coef * (i - j) // (j + 1)
        tree_str += "\n"
    return tree_str+" "*row+"|\n"+" "*row+"|"
    


print(custom_christmas_tree("*@o",4))