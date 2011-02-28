$.fn.highlight = function(words) {
    var TEXT_NODE = 3;
    var NOT_TEXT_NODE = 1;
    
    function highlightWordInTextNode(textNode, word) {
        var splitPoint = textNode.data.indexOf(word);
        if (splitPoint >= 0) {
            var left = textNode;
            var middle = textNode.splitText(splitPoint);
            var right = middle.splitText(word.length);
                    
            // Create an element that will hold the highlighted text
            // and replace the middle element with this new one.
            var highlightSpan = document.createElement('span');
            highlightSpan.className = 'highlight';
            highlightSpan.appendChild(document.createTextNode(word));
            left.parentNode.replaceChild(highlightSpan, middle);
                    
            // recurse on the right branch if it's not empty
            right.data && highlightWordInTextNode(right, word)
        }
    }
    
    function findAndHighlightTextNodes(node, word) {
        if (node.nodeType == TEXT_NODE) {
            highlightWordInTextNode(node, word);
        }
        else if (node.nodeType == NOT_TEXT_NODE) {
            $.each(node.childNodes, function(){
                findAndHighlightTextNodes(this, word);
            })
        }
    }
    
    if (typeof words == 'string') {words = Array(words);}
    
    var jNodes = this;
    //TODO: be more efficient
    $.each(words, function(idx, word){
        jNodes.each(function(){findAndHighlightTextNodes(this, word)});
    });
}

function searchAllInstancesInString(haystack, needle) {
    ret = Array();
    offset = 0;
    while(haystack.indexOf(needle, offset) >= 0) {
        ret.push(haystack.indexOf(needle, offset));
        offset += needle.length;
    }
    return ret;
}
