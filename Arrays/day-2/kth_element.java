//Find the "Kth" max and min element of an array 


import java.util.*;
public class kth_element{
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int size=sc.nextInt();
        int k=sc.nextInt();
        int[] array=new int[size];
        for(int i=0;i<size;i++){
            array[i]=sc.nextInt();
        }
        Arrays.sort(array);
        System.out.print(array[k-1]+" ");
        System.out.println(array[size-k]);
    }
}
