#include <stdio.h>
#include <stdlib.h>


void max_sum(int *array, int cols, int *start, int *end, int *sum){
    /**
    Given an array, this function will find out the maximum sum of its contiguous elements.
    e.g. given, 1,-2,3,5 - Max sum = 8 (3,5)  
    */  
    int curr, i;
    *sum = 0;
    //Sum is the max recorded sum
    //curr is the currently observed sum
    curr = 0;
    *start = *end = 0;
    int iterator = 0;
    for(i = 0; i<cols; i++)
    {
        /**
        Algorithm - 
		We calculate the current sum of contiguous elements by adding the next element to the current sum.
		If current observed sum > maximum sum so far, we update the max value (and the start and end pointers) and go on.
        If the current falls below 0, we know it can't be a part of max sum elements, 
		so we update current sum to 0 and the start iterator to the element net to the one being scanned and continue the traversal. 
		Complexity - O(n)
		*/
	curr = curr + *(array+i);
        if(curr > *sum)
        {
            *sum = curr;
            *end = i;
            *start = iterator;
        }
        if (curr < 0)
        {
            curr = 0;
            iterator = i + 1;
        }
    }
}

int main(){
  /** Variable declaration and initialization 
  We will use a double pointer to hold the 2D matrix
  for dynamic allocation of space.
  */
  int **matrix;
  int *array;
  int rows,cols,i,j,temp,k;

  int row1,row2,col1,col2,start,end,max_so_far;
  int sum = 0;  
  int flag = 0;

  row1 = -9999;
  row2 = row1;
  col1 = row1;
  col2 = row1; 
  start = row1;
  end = row1;
  max_so_far = -1;
  matrix = NULL;
  /**
  We first ask the user about the desired Matrix size, 
  making sure that they input the right values.
  */
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
  /**
  Now that we know the size, we dynamically allocate memory of that size
  to hold the matrix elements.
  */
 
  /**
  The way we do this is to consider a matrix as an array of arrays.
  Every array will hold elements equal to Column size and there would be
  'Row' number of such arrays.
  */

  //Allocating memory for 'Row' arrays
  matrix = (int**)malloc(rows*sizeof(int*));
  //Now allocating memory for each array of 'Column' elements itself
  for(i=0;i<rows;i++){
      		*(matrix+i) = (int*)malloc(cols*sizeof(int));
  }

  //building the matrix by taking user input
  
  for(i=0;i<rows;i++){//Complexity O(n^2)
	for(j=0;j<cols;j++){
		printf("\nEnter Matrix[%d][%d] :",i,j);
		if(scanf("%d",&temp) != 1){
		 	printf("\nInvalid Input! Exiting..");
		}
		if(temp > 0)
			flag = 1;
		*(*(matrix+i)+j) = temp;
        }         
  }

  if(flag == 0){
    	printf("\nWe require at least 1 positive value for this algorithm to work! Please try again.\n");
	exit(-1);
  }

  //Print Matrix
  printf("\nYour Matrix is:\n");
  for(i=0;i<rows;i++){
	printf("\n");
        for(j=0;j<cols;j++){
                printf("\t%d",*(*(matrix+i)+j));
        }
  }
  printf("\n");
  
  /**
  Algorithm:
  1. We first traverse the matrix row by row - 
	 while doing this, we consider a temporary array (of size 'Column' 
		this array holds the sum of elements in each column of the row below.
     e.g. If our Matrix looks like: 1 2 3 
                                    4 5 6 
                                    7 8 9 
          when we are at row 0, the temp array will hold: [1+4+7,2+5+8,3+6+8] and so on.
  2. With this array in place, we then find out the maximum sum of contiguous elements (start and end)
     and record it. If on further iteration, we find a sum greater than earlier, we update the value
     and the start and end coordinates. 
  3. The max sum recorded at the end of all iterations and the i,j (See loop below) start,end values 
     give us the matrix that has the highest sum of elements. 
  Note: This Algorithm only works if at least one matrix element is positive.
  Complexity : O(n^3)
  */
 
  //Create the temporary array
  array = (int*)malloc(cols*sizeof(int));
  
  //Now we find the greatest sum

  for(i=0;i<rows;i++){
  
	for(k=0;k<cols;k++){
		//everything is 0 to start with
		*(array+k) = 0;
	}
        for(j=i;j<rows;j++){
		for(k=0;k<cols;k++)
			*(array+k) = *(array+k)+ *(*(matrix+j)+k);
  		//Now that we have the Array, find the maximum sum and the contiguous elements.
		max_sum(array,cols,&start,&end,&sum);
		if(sum > max_so_far){
 			col1 = start;
			col2 = end;
			row1 = i;
 			row2 = j;
			max_so_far = sum;
  		}
        }
  }

  //What we have now is the solution. 

  printf("Max sum is: %d, start_row = %d, start_col = %d, end_row = %d, end_col = %d\n",max_so_far,row1,col1,row2,col2);
  return 0;
}




