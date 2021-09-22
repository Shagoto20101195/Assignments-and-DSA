import java.util.*;
public class Task5a
{
  public static void print_col(int n, int count)
  {
    if(n > count)
    {
      System.out.println();
      return;
    }
    
    System.out.print(n);
    print_col(n + 1, count);
  }
  
  public static void print_row(int n, int count)
  {
    if(count == 0)
    {
      return;
    }
    
    print_col(1, n - count + 1);
    print_row(n, count-1);
  }
  
  public static void main(String [] args)
  {
    Scanner read = new Scanner(System.in);
    
    int n = read.nextInt();
    print_row(n, n);
  }
}