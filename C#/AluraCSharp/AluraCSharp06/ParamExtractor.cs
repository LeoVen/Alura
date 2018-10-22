using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AluraCSharp06
{
    class ParamExtractor
    {
        public string URL { get; }
        private readonly string _arguments;

        public ParamExtractor(string url)
        {
            if (string.IsNullOrEmpty(url))
                throw new ArgumentException("URL must not empty or null.", nameof(url));

            _arguments = url.Substring(url.IndexOf('?') + 1);

            URL = url;
        }

        public string GetValue(string paramName)
        {
            string term = paramName + "=";

            int index = _arguments.IndexOf(term);

            return _arguments.Substring(index + term.Length);
        }
    }
}
