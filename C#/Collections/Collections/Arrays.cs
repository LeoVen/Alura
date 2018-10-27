using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class Arrays
    {
        public static void ArrayTest()
        {
            // myType[] varName = new myType[N];
            int[] arrays = new int[20];

            for (var i = 0; i < arrays.Length; i++)
                arrays[i] = i;

            foreach (var item in arrays)
            {
                Console.Write($"{item} ");
            }
        }

        public static void ArrayFunctions()
        {
            int[] myArray = new int[20];

            for (var i = 0; i < myArray.Length; i++)
                myArray[i] = i;

            DisplayArray(myArray, "Original Array");

            Array.Reverse(myArray);
            DisplayArray(myArray, "Reversed Array");

            Array.IndexOf(myArray, 19);

            Array.Resize(ref myArray, 40);
            DisplayArray(myArray, "Resized array to 40");

            Array.Sort(myArray);
            DisplayArray(myArray, "Sorting Array");

            int[] anotherArray = new int[20];
            Array.Copy(myArray, 20, anotherArray, 0, myArray.Length - 20);
            DisplayArray(anotherArray, "Copy from 20 to Length");

            int[] array = anotherArray.Clone() as int[];
            if (array != null)
                DisplayArray(array, "Cloned array");

            Array.Clear(anotherArray, 0, 9);
            DisplayArray(anotherArray, "Cleared from 0 to 9");
        }

        public static void DisplayArray<T>(T[] array, string phrase)
        {
            Console.WriteLine(phrase);
            for (var i = 0; i < array.Length; i++)
                Console.Write($"{array[i]} ");

            Console.WriteLine(" ");
        }
    }
}
