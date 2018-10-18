using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp04
{
    class EvilNumberException : Exception
    {
        public string Reason { get; private set; }

        public EvilNumberException(string message) : base(message)
        {
            this.Reason = "There are certain numbers that are evil...";
        }
    }
}
