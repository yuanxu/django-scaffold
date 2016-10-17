/**
 * 公式编辑器
 */

KindEditor.lang({
    formula : '公式编辑器'
}, 'zh_CN');

KindEditor.plugin('formula', function(K) {
    var editor = this;
    var name = 'formula';

    // 点击图标时打开编辑器
    editor.clickToolbar(name, function() {
        showDialog();
    });

    //显示编辑器
    function showDialog(){
        var dialog = KindEditor.dialog({
            width : 340,
            height:300,
            title : '公式编辑器',
            body : '<iframe marginwidth="0" id="formula-dialog" frameborder="no" src="'+editor.basePath+'plugins/formula/dialog.html" width="340px" height="265px"></iframe>',
            closeBtn : {
                name : '关闭',
                click : function(e) {
                    dialog.remove();
                }
            },
            yesBtn : {
                name : '确定',
                click : function(e){
                    addFormula();
                    dialog.remove();
                }
            },
            noBtn : {
                name : '取消',
                click : function(e) {
                    dialog.remove();
                }
            }

        });
    }
    //添加公式到编辑器中
    function addFormula(){
        var thedoc = document.getElementById('formula-dialog').contentDocument;

        var mathHtml = thedoc.getElementById("formula").innerHTML;

        mathHtml = mathHtml.replace('<span class="textarea"><textarea></textarea></span>','');
        mathHtml = '<span class="mathquill-rendered-math" style="font-size:16px;" >' + mathHtml + '</span><span>&nbsp;</span>';
        editor.insertHtml(mathHtml);
    }


});

