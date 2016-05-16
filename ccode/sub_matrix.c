#include <stdio.h>
#include <stdlib.h>


void max_sum(int *array, int cols, int &start, int &end, int &sum){

    int curr, i;
    sum = 0;
    curr = 0;
    start = end = 0;
    int lx1, lx2;
    lx1 = 0;
    for(int i = 0; i<n; i++)
    {
        curr = curr + *(array+i);
        if(curr > sum)
        {
            sum = curr;
            end = i;
            start = lx1;
        }
        if (curr < 0)
        {
            curr = 0;
            lx1 = i + 1;
        }
    }
}

int main(){

  int **matrix;
  int *array;
  int rows,cols,i,j,temp,k;

  int row1 = row2 = col1 = col2 = start = end = max_so_far = -1;

  printf("\nBuilding a MxN matrix. (M can be == N)\n");
  printf("\nEnter the number of rows :");
  if(scanf("%d",&rows) != 1){
  	printf("\nInvalid Input! Exiting..");
	exit(-1);
  }
  printf("\nEnter the number of columns:");
  if(scanf("%d",&cols) != 1){
	printf("\nInvalid Input! Exiting..");
	exit(-1);
  }
  matrix = NULL;  
  matrix = malloc(rows*sizeof(int*));
  
  for(i=0;i<rows;i++){
      		*(matrix+i) = malloc(cols*sizeof(int));
  }

  //building the matrix
  
  for(i=0;i<rows;i++){
	for(j=0;j<cols;j++){
		printf("\nEnter Matrix[%d][%d] :",i,j);
		if(scanf("%d",&temp) != 1){
		 	printf("\nInvalid Input! Exiting..");
		}
		*(*(matrix+i)+j) = temp;
        }         
  }

  //Print Matrix
  print("\nYour Matrix is:\n");
  for(i=0;i<rows;i++){
	printf("\n");
        for(j=0;j<cols;j++){
                printf("\t%d",*(*(matrix+i)+j));
        }
  }
  print("\n");
  //Inititalize the temporary array
  array = malloc(cols*sizeof(int));
  
  //Now we find the greatest sum

  for(i=0;i<rows;i++){
  
	for(k=0;k<cols;k++){
		*(array+k) = 0;
	}
        for(j=i;j<rows;j++){
		for(k=0;k<cols;k++)
			*(array+k) = *(array+k)+ *(*(matrix+j)+k);
  		max_sum(array,cols,start,end,sum);
		if(sum > max_so_far){
 			col1 = start;
			col2 = end;
			row1 = i;
 			row2 = j;
			max_so_far = sum;
  		}
        }
  }
  print("Max sum is: %d, start_row = %d, start_col = %d, end_row = %d, end_col = %d",max_so_far,row1,col1,row2,col2);
  return 0;
}




