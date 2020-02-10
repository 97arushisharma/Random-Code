object HelloWorld {
    
    def processReferer(url : String): String = {
        var referer : String = url
        if (referer.startsWith("http:")){
          referer = referer.substring(5).replaceAll("^[/]+|[/]+$", "")
          return processReferer(referer)
        }
        if (referer.startsWith("https:")){
          referer = referer.substring(6).replaceAll("^[/]+|[/]+$", "")
          return processReferer(referer)
        }
        if (referer.startsWith("ftp:")){
          referer = referer.substring(4).replaceAll("^[/]+|[/]+$", "")
          return processReferer(referer)
        }
        if (referer.startsWith(":")){
          referer = referer.substring(1).replaceAll("^[/]+|[/]+$", "")
          return processReferer(referer)
        }
        referer = referer.replaceAll("//","/")
        if(referer.startsWith("/")) referer.split("/")(1)
        else referer.split("/")(0)
    }
      
    
   def main(args: Array[String]) {
      
      
        var str : String = "http://yvp.yumenetworks.com/[[IMPORT]]/njpl.yumenetworks.com/include/advertiser/http://component_as3.swf16" 
        var str1 : String = "http:www.taptica.com60"
        var str2 : String = "http:/53"
        var str3 : String = "https://https://secure.netflix.com/us/tvui/release-2016_02_29-46/13_3/sapphire/720p/gibbon/signupwizard.js?nrdjsSuffix=nrdjs%2Fv2.21.7-23"
        var str4 : String = "://yytingting.com62"
        var str5 : String = "https://www-m.cnn.com/2018/05/23/europe/yulia,skripal-nerve-agent-recovery-intl/index.html49"
        var str6 : String = "ftp:/abcdefgh.edu/hello"
        var str7 : String = "ftp://http://http://[fdf8:f53b:82e4::53]"
        //String[] arrOfStr = str.split("http://|https://|,",2);
        var hostname : String = processReferer(str7)
        println("..."+hostname+"...")
      
      
      
   }
}
