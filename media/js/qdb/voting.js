
function loadDoc(url, callback) {
   // branch for native XMLHttpRequest object
   try {
      if (window.XMLHttpRequest) {
         req = new XMLHttpRequest();
         req.onreadystatechange = (function(){ processReqChange(req, callback); })
         req.open("GET", url, true);
         req.send(null);
      // branch for IE/Windows ActiveX version
      } else if (window.ActiveXObject) {
         isIE = true;
         req = new ActiveXObject("Microsoft.XMLHTTP");
         if (req) {
            req.onreadystatechange = (function(){ processReqChange(req, callback); })
            req.open("GET", url, true);
            req.send();
         }
      }        
   } catch (e) {
      window[callback](e.message);
   }
}
                
// handle onreadystatechange event of req object
function processReqChange(req, callback) {
   // only if req shows "loaded"
   if ( req.readyState == 4 ) {     
      if ( req.statusText == "OK" ) {
         window[callback](req.responseText);
      } else {
         window[callback]("Error fetching data: " + req.statusText);
      }
   }
}
                
function upvote(id) {
   loadDoc('/qdb/quote/'+id+'/up', 'updatescore');
} 
function downvote(id) {
   loadDoc('/qdb/quote/'+id+'/down', 'updatescore');
}

function updatescore(response) {
   document.getElementById("score").innerHTML = response;
}
