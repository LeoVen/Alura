using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class LINQ
    {
        public static void Test01()
        {
            List<Month> months = new List<Month>()
            {
                new Month("January", 31),
                new Month("February", 28),
                new Month("March", 31),
                new Month("April", 30),
                new Month("May", 31),
                new Month("June", 30),
                new Month("July", 31),
                new Month("August", 31),
                new Month("September", 30),
                new Month("October", 31),
                new Month("November", 30),
                new Month("December", 31)
            };

            IEnumerable<string> query = months
                .Where(m => m.Days == 31)
                .OrderBy(m => m.Name)
                .Select(m => m.Name.ToUpper());

            foreach (var item in query)
            {
                Console.WriteLine(item);
            }
        }
    }

    class Month
    {
        public Month(string name, int days)
        {
            Name = name;
            Days = days;
        }

        public string Name { get; private set; }
        public int Days { get; private set; }

        public override string ToString()
        {
            return $"{Name} - {Days}";
        }
    }
}
