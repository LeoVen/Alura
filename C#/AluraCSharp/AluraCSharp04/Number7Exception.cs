using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp04
{
    class Number7Exception : EvilNumberException
    {
        public string Reason { get; private set; }

        public Number7Exception(string message) : base(message)
        {
            this.Reason = "The number 7 is evil and brings bad luck!";
        }
    }
}
