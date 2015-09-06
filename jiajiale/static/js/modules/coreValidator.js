/*** author: guiche ***/
/*** 2015.01.21 ***/

define(["jquery"], function($) {
    return {
        clearVal: function( $this ) {
            $this.next().html('');
        },
        validateVal: function( $this ) {
            var validateList = [{
                    name: "isEmail",
                    expression: /^\w+([\.\-]\w+)*\@\w+([\.\-]\w+)*\.\w+$/,
                    message: "亲，邮箱格式好像错了哦"
                }, {
                    name: "isQQ",
                    expression: /^\d{5,}$/,
                    message: "亲，是不是QQ号错了呢"
                }, {
                    name: "isInt",
                    expression: /^\d*$/,
                    message: "亲，是整数哦"
                }, {
                    name: "isDate",
                    expression: /^(\d{4})\-(\d{2})\-(\d{2})$/,
                    message: "日期格式不正确"
                }, {
                    name: "isDateShort",
                    expression: /^(\d{4})\-(\d{2})\-(\d{2}) (\d{2}):(\d{2}):(\d{2})$/,
                    message: "日期格式不正确"
                }, {
                    name: "isLetter",
                    expression: /^[a-zA-Z]+$/,
                    message: "必须为英文字母"
                }, {
                    name: "isTel",
                    expression: /^1[3|4|5|7|8][0-9]\d{8}$/,
                    message: "亲，手机号是不是记错了呢"
                }, {
                    name: "isAccount",
                    expression: /^[a-zA-Z][a-zA-Z0-9_]{5,19}$/,
                    message: "必须以字母开头，且是数字、字母、下划线的6-20位组合"
                }, {
                    name: "isUrl",
                    expression: /a-zA-z]+:\/\/[^\s]*/,
                    message: "网址格式不正确"
                }, {
                    name: "isIDCard",
                    expression: /d{18}|d{15}/,
                    message: "身份证号必须为15或18位数字"
                }, {
                    name: "isNull",
                    expression: /\S/,
                    message: "这里不能空着哦"
                }];
            var $validateType = $this.data( 'validate_type' ),
                val = $this.val();

            if ( $validateType === undefined ) {
                return false;
            };
            $.each( validateList, function( i,e ){
                if( $validateType == e.name ) {
                    var regexp = e.expression;
                    if( !( regexp.test( val ) ) ) {
                        $this.next().html( e.message );
                    };
                }
            });
        }
    };
});
