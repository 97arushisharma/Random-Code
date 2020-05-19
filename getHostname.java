public class getHostname { 
    
    public static String processURLforHostname(String url){
            if (url.startsWith("http:")){
                    url = url.substring(5).replaceAll("^[/]+|[/]+$", "");
                    return processURLforHostname(url);
            }
            if (url.startsWith("https:")){
                    url = url.substring(6).replaceAll("^[/]+|[/]+$", "");
                    return processURLforHostname(url);
            }
            if (url.startsWith("ftp:")){
                    url = url.substring(4).replaceAll("^[/]+|[/]+$", "");
                    return processURLforHostname(url);
            }
            if (url.startsWith(":")){
                    url = url.substring(1).replaceAll("^[/]+|[/]+$", "");
                    return processURLforHostname(url);
            }
            url = url.replaceAll("//","/");
            if(url.startsWith("/")){
                    return processURLforHostname(url.replaceAll("^[/]+|[/]+$", ""));
            }else{
                    return url.split("/")[0];
            }
    }

    
    public static void main(String args[]) 
    { 
        
        
        String str = "http://yvp.yumenetworks.com/[[IMPORT]]/njpl.yumenetworks.com/include/advertiser/http://component_as3.swf16"; 
        String str1 = "www.taptica.com60";
        String str2 = "http:/53";
        String str3 = "https://https://secure.netflix.com/us/tvui/release-2016_02_29-46/13_3/sapphire/720p/gibbon/signupwizard.js?nrdjsSuffix=nrdjs%2Fv2.21.7-23";
        String str4 = "://yytingting.com62";
        String str5 = "/";
        //String[] arrOfStr = str.split("http://|https://|,",2);
        String hostname = processURLforHostname(str4);
        System.out.println(hostname);
  
        // for (String a : arrOfStr){ 
        //     System.out.println(a);
        //     System.out.println("->");
        // }
    } 
}
