# include <stdio.h>  
 
char * reverse_string(char *string)
/*对字符串进行翻转*/
{
    printf("%s\n", string);
    char temp;
    char *top = string;
    char *end = string;
    while (*end != '\0')
    {
        printf("%c\n", *end);
        end++;
    }
    end--;
    printf("%c\n", *end);
 
    for (; top < end; (top ++ && end--))
    {
        temp = *top;
        *top = *end;
        *end = temp;
    }
    return string;
}
int main()
{
    char a[] = "123456";
    printf("%s\n", reverse_string(a));
    return 0;
}