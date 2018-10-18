using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp04
{
    class Program
    {
        static void Main(string[] args)
        {
            int total = 0;

            try
            {
                for (int i = 200, j = 10; ; i++, j--)
                {
                    total = myMethod(total, i, j);
                }
            }
            catch (DivideByZeroException e)
            {
                Console.WriteLine("Ops! Division by 0");
                Console.WriteLine(e.StackTrace);
                Console.WriteLine(e.GetType());
            }
            finally
            {
                Console.WriteLine("\n\nWhen the exception was thrown the variable total had a value of " + total);
            }

            try
            {
                for (int i = 0, j = 10; i < 10; i++, j--)
                    SpecialFunction(i, j);
            }
            catch (Number4Exception e)
            {
                Console.WriteLine(e.Message);
                Console.WriteLine(e.Reason);
            }
            catch (Number7Exception e)
            {
                Console.WriteLine(e.Message);
                Console.WriteLine(e.Reason);
            }

            // ArgumentException, ParamName and nameof

            // StackTrace

            // Inner Exception

            // Using

            Console.ReadLine();
        }

        private static int myMethod(int total, int i, int j)
        {
            try
            {
                total += i / j;
            }
            catch (DivideByZeroException)
            {
                Console.WriteLine("Invalid division at myMethod(): i = " + i + ", j = " + j);
                throw; // Throws the catched exception back
            }

            return total;
        }

        private static void SpecialFunction(int i, int j)
        {
            if (i == 4)
                throw new Number4Exception("The number 4 is evil! Not allowed in here!");

            if (i == 7)
                throw new Number7Exception("The number 7 is evil! Not allowed in here!");

            Console.WriteLine("I like the number " + i);
        }
    }
}
