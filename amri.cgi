#!/usr/bin/gawk -f
BEGIN {
    print "Content-type: text/plain\n\n"

    ARGV[ARGC++] = "/home/l4rge/public_html/l4rge.com/p/r/o/properteer/dom-file"
}


## Check rank in google, msn and yahoo

# Main program

{

    kw = tolower($0)
    kwcat = ""
    for (kwcat_i = 1; kwcat_i <= NF; kwcat_i++)
	kwcat = kwcat $kwcat_i
    kwcat = tolower(kwcat)
    for(time=1; time<=20000000; time++) continue
    print kwcat
    kwdom = kwcat ".org"

    g100 = get_google_100_results(kw)
    l50 = get_live_50_results(kw)
    y100 = get_yahoo_100_results(kw)

    #print g100 l50 y100

    g_urls = extract_google_urls(g100)
    l_urls = extract_live_urls(l50)
    y_urls = extract_yahoo_urls(y100)

    #print g_urls l_urls y_urls

    g_pos =  find_site_position(g_urls,kwdom)
    l_pos =  find_site_position(l_urls,kwdom)
    y_pos =  find_site_position(y_urls,kwdom)

    ranks = ranks kw "," g_pos "," l_pos "," y_pos "\n"
}

END {
    print "KW,Google,Live,Yahoo"
    print ranks

}
# extract google urls
# ---------------------------
   
function extract_google_urls(serp_results,    a,i,n,urls)
{


    n = split(serp_results  , a, "<cite>|</cite>")
    
    for (i=2; i<n; i += 2){

	$0 = a[i]

	gsub(/<b>|<\/b>/, "")
    
	urls = urls $0"\n"

    }

    return urls
}# extract live urls
# ---------------------------
   
function extract_live_urls(serp_results,    a,i,n,urls)
{


    n = split(serp_results  , a, "<cite>|</cite>")
    
    for (i=2; i<n; i += 2){

	$0 = a[i]

	gsub(/<strong>|<\/strong>/, "")
    
	urls = urls $0"\n"

    }

    return urls
}# extract yahoo urls
# ---------------------------
function extract_yahoo_urls(serp_results,    a,i,n,urls)
{


    n = split(serp_results  , a, "<span class=url>|</span>")
    
    for (i=2; i<n; i += 2){

	$0 = a[i]
	if ($0 ~ /class="sm-myappicn|class="scroll|class="sslink|class="tgrad|class="ftpromo|class="sm-ctl-b/) continue
	if ($0 == "</a>") continue
	gsub(/<b>|<\/b>/, "")
	gsub(/<wbr>|<wbr \/>/, "")
    
	urls = urls $0"\n"

    }

    return urls

}# find site/domain position among urls
# -------------------------------------
   
function find_site_position(urls,kwdom,    a,i,n,pos,f,dotkwdom,position)
{


    n = split(urls  , a, "\n")
    
    for (i=1; i<=n; i++){

	$0 = a[i]
	dotkwdom = "."kwdom
	if ( index($0, kwdom) == 1 || index($0, dotkwdom) > 1 ) {
	    pos = i
	    if (n > 90) {
		f = n - 101
		pos = pos - f
	    }
	    else {
		f = n - 51
		pos = pos -f + 7 # patched for 7 positions error
	    }
	    position = position " " pos 

	}

	#else pos = ""

    }
    
    return position
}# Get Google first 100 SERP results
# ----------------------------------   

function get_google_100_results(kwd,  kwd_g_url,host,url,HttpService,results)
{
    ORS = "\r\n"

    kwd_g_url = gensub( / / , "+" , "g" , kwd )
      
    host = "www.google.com"
    url = "/search?hl=en&as_q="kwd_g_url"&as_epq=&as_oq=&as_eq=&num=100&lr=&as_filetype=&ft=i&as_sitesearch=&as_qdr=all&as_rights=&as_occt=any&cr=&as_nlo=&as_nhi=&safe=images"

    HttpService = "/inet/tcp/0/"host"/80"
       
    print "GET "url" " "\r\n"   |& HttpService
    #print "GET "url "HTTP/1.0"  "\r\n"   |& HttpService
    #print "Host: "host    |& HttpService
    #print "User-Agent: Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092510 Ubuntu/8.04 (hardy) Firefox/3.0.3"    |& HttpService
    #print "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"    |& HttpService
    #print "Accept-Language: en-us,en;q=0.5"    |& HttpService
    #print "Accept-Encoding: gzip,deflate"    |& HttpService
    #print "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7"    |& HttpService
    #print "Keep-Alive: 300"    |& HttpService
    #print "Connection: keep-alive"    |& HttpService

    while ((HttpService |& getline) > 0)
	results = results $0
    close(HttpService)
    ORS = "\n" # reset ORS back to its default value
    
    return results
}# Get Live first 50 SERP results
# ----------------------------------   

function get_live_50_results(kwd,  kwd_l_url,host,url,HttpService,results)
{
    ORS = "\r\n"

    kwd_l_url = gensub( / / , "+" , "g" , kwd )
      
    host = "search.live.com"
    url = "/results.aspx?q="kwd_l_url"&go=&form=QBRE"

    HttpService = "/inet/tcp/0/"host"/80"
       
    print "GET "url " HTTP/1.0"     |& HttpService
    print "User-Agent: TinyBrowser/2.0 (TinyBrowser Comment; rv:1.9.1a2pre) Gecko/20201231"     |& HttpService
    #print "User-Agent: curl/7.18.2 (x86_64-pc-linux-gnu) libcurl/7.18.2 OpenSSL/0.9.8g zlib/1.2.3.3 libidn/1.8"     |& HttpService
    print "Host: search.live.com"     |& HttpService
    print "Cookie: mkt1=norm=en-US; MUID=2E984DC0EFFA42509FAB500FD6DA1584; OVR=flt=0&PerfTracking=0&DomainVertical=0&Cashback=0&MSCorp=kiev; SRCHD=D=619947&AF=NOFORM; mkt2=ui=en-US; AFORM=NOFORM; RMS=T=370; SRCHSESS=GUID=6A627456C20E42578542445D0BF920FA&TS=1236342516; SRCHUID=V=2&GUID=3364BA1D822C4E16B255155DC58C9F3A; SRCHUSR=AUTOREDIR=0&GEOVAR=&DOB=20090306; AS=1; culture=a=0; SRCHHPGUSR=NEWWND=0&ADLT=DEMOTE&NRSLT=50&NRSPH=2&LOC=LAT%3d28.53|LON%3d-81.38|DISP%3dOrlando%2c%20Florida|&SRCHLANG="   |& HttpService
    print "Accept: */*"  "\r\n"   |& HttpService

    while ((HttpService |& getline) > 0)
	results = results $0
    close(HttpService)
    ORS = "\n" # reset ORS back to its default value
    
    return results
}# Get Yahoo first 100 SERP results
# ----------------------------------   

function get_yahoo_100_results(kwd,  kwd_y_url,host,url,HttpService,results)

{
    ORS = "\r\n"

    kwd_y_url = gensub( / / , "+" , "g" , kwd )
      
    host = "search.yahoo.com"
    url = "/search;_ylt=A0geu_NCGbFJlVcBpclXNyoA?p="kwd_y_url"&y=Search&fr=yfp-t-501&n=100&vm=p&vs=&vf=all "

    HttpService = "/inet/tcp/0/"host"/80"
       
    print "GET "url "\r\n"    |& HttpService
    #print "GET "url "HTTP/1.0"     |& HttpService
    print "Host: "host    |& HttpService
    print "User-Agent: Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092510 Ubuntu/8.04 (hardy) Firefox/3.0.3"    |& HttpService
    print "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"    |& HttpService
    print "Accept-Language: en-us,en;q=0.5"    |& HttpService
    print "Accept-Encoding: gzip,deflate"    |& HttpService
    print "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7"    |& HttpService
    print "Keep-Alive: 300"    |& HttpService
    print "Connection: keep-alive"    |& HttpService
    print "Cookie: B=c2o7ejd4r264c&b=3&s=02; HP=1; sSN=BmSGitU2wWGEPzvoPvyn9aUXur1699znYUZxBI0kHvMn2R46zyiuDX_dFG9CujyV3V1rKurkhuS1eYXsM96xJg--; sSM=hsb=50&_n=1" "\r\n"  |& HttpService
    while ((HttpService |& getline) > 0)
	results = results $0
    close(HttpService)
    ORS = "\n" # reset ORS back to its default value
    
    return results
}