using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp08
{
    public static class ListExtensions
    {
        public static void AddAll<T>(this List<T> list, params T[] elements)
        {
            foreach (T item in elements)
            {
                list.Add(item);
            }
        }
    }
}
