from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String, \
     Error, Generic, Number, Operator


class YourStyle(Style):

    styles = {
        Token:                  '',
        Comment:                'italic #888',
        Keyword:                'bold #005',
        Name:                   '#f00',
        Name.Class:             'bold #0f0',
        Name.Function:          '#0f0',
        String:                 'bg:#eee #111'
    }
    
.highlight pre {
    line-height: 125%;
}

.highlight td.linenos .normal {
    color: inherit;
    background-color: transparent;
    padding-left: 5px;
    padding-right: 5px;
}

.highlight span.linenos {
    color: inherit;
    background-color: transparent;
    padding-left: 5px;
    padding-right: 5px;
}

.highlight td.linenos .special {
    color: #000000;
    background-color: #ffffc0;
    padding-left: 5px;
    padding-right: 5px;
}

.highlight span.linenos.special {
    color: #000000;
    background-color: #ffffc0;
    padding-left: 5px;
    padding-right: 5px;
}

.highlight .hll {
    background-color: #ffffcc
}

.highlight {
    background: #f8f8f8;
}

.highlight .c {
    color: #8f5902;
    font-style: italic
}

/* Comment */
.highlight .err {
    color: #a40000;
    border: 1px solid #ef2929
}

/* Error */
.highlight .g {
    color: #000000
}

/* Generic */
.highlight .k {
    color: #204a87;
    font-weight: bold
}

/* Keyword */
.highlight .l {
    color: #000000
}

/* Literal */
.highlight .n {
    color: #000000
}

/* Name */
.highlight .o {
    color: #ce5c00;
    font-weight: bold
}

/* Operator */
.highlight .x {
    color: #000000
}

/* Other */
.highlight .p {
    color: #000000;
    font-weight: bold
}

/* Punctuation */
.highlight .ch {
    color: #8f5902;
    font-style: italic
}

/* Comment.Hashbang */
.highlight .cm {
    color: #8f5902;
    font-style: italic
}

/* Comment.Multiline */
.highlight .cp {
    color: #8f5902;
    font-style: italic
}

/* Comment.Preproc */
.highlight .cpf {
    color: #8f5902;
    font-style: italic
}

/* Comment.PreprocFile */
.highlight .c1 {
    color: #8f5902;
    font-style: italic
}

/* Comment.Single */
.highlight .cs {
    color: #8f5902;
    font-style: italic
}

/* Comment.Special */
.highlight .gd {
    color: #a40000
}

/* Generic.Deleted */
.highlight .ge {
    color: #000000;
    font-style: italic
}

/* Generic.Emph */
.highlight .gr {
    color: #ef2929
}

/* Generic.Error */
.highlight .gh {
    color: #000080;
    font-weight: bold
}

/* Generic.Heading */
.highlight .gi {
    color: #00A000
}

/* Generic.Inserted */
.highlight .go {
    color: #000000;
    font-style: italic
}

/* Generic.Output */
.highlight .gp {
    color: #8f5902
}

/* Generic.Prompt */
.highlight .gs {
    color: #000000;
    font-weight: bold
}

/* Generic.Strong */
.highlight .gu {
    color: #800080;
    font-weight: bold
}

/* Generic.Subheading */
.highlight .gt {
    color: #a40000;
    font-weight: bold
}

/* Generic.Traceback */
.highlight .kc {
    color: #204a87;
    font-weight: bold
}

/* Keyword.Constant */
.highlight .kd {
    color: #204a87;
    font-weight: bold
}

/* Keyword.Declaration */
.highlight .kn {
    color: #204a87;
    font-weight: bold
}

/* Keyword.Namespace */
.highlight .kp {
    color: #204a87;
    font-weight: bold
}

/* Keyword.Pseudo */
.highlight .kr {
    color: #204a87;
    font-weight: bold
}

/* Keyword.Reserved */
.highlight .kt {
    color: #204a87;
    font-weight: bold
}

/* Keyword.Type */
.highlight .ld {
    color: #000000
}

/* Literal.Date */
.highlight .m {
    color: #0000cf;
    font-weight: bold
}

/* Literal.Number */
.highlight .s {
    color: #4e9a06
}

/* Literal.String */
.highlight .na {
    color: #c4a000
}

/* Name.Attribute */
.highlight .nb {
    color: #204a87
}

/* Name.Builtin */
.highlight .nc {
    color: #000000
}

/* Name.Class */
.highlight .no {
    color: #000000
}

/* Name.Constant */
.highlight .nd {
    color: #5c35cc;
    font-weight: bold
}

/* Name.Decorator */
.highlight .ni {
    color: #ce5c00
}

/* Name.Entity */
.highlight .ne {
    color: #cc0000;
    font-weight: bold
}

/* Name.Exception */
.highlight .nf {
    color: #000000
}

/* Name.Function */
.highlight .nl {
    color: #f57900
}

/* Name.Label */
.highlight .nn {
    color: #000000
}

/* Name.Namespace */
.highlight .nx {
    color: #000000
}

/* Name.Other */
.highlight .py {
    color: #000000
}

/* Name.Property */
.highlight .nt {
    color: #204a87;
    font-weight: bold
}

/* Name.Tag */
.highlight .nv {
    color: #000000
}

/* Name.Variable */
.highlight .ow {
    color: #204a87;
    font-weight: bold
}

/* Operator.Word */
.highlight .pm {
    color: #000000;
    font-weight: bold
}

/* Punctuation.Marker */
.highlight .w {
    color: #f8f8f8
}

/* Text.Whitespace */
.highlight .mb {
    color: #0000cf;
    font-weight: bold
}

/* Literal.Number.Bin */
.highlight .mf {
    color: #0000cf;
    font-weight: bold
}

/* Literal.Number.Float */
.highlight .mh {
    color: #0000cf;
    font-weight: bold
}

/* Literal.Number.Hex */
.highlight .mi {
    color: #0000cf;
    font-weight: bold
}

/* Literal.Number.Integer */
.highlight .mo {
    color: #0000cf;
    font-weight: bold
}

/* Literal.Number.Oct */
.highlight .sa {
    color: #4e9a06
}

/* Literal.String.Affix */
.highlight .sb {
    color: #4e9a06
}

/* Literal.String.Backtick */
.highlight .sc {
    color: #4e9a06
}

/* Literal.String.Char */
.highlight .dl {
    color: #4e9a06
}

/* Literal.String.Delimiter */
.highlight .sd {
    color: #8f5902;
    font-style: italic
}

/* Literal.String.Doc */
.highlight .s2 {
    color: #4e9a06
}

/* Literal.String.Double */
.highlight .se {
    color: #4e9a06
}

/* Literal.String.Escape */
.highlight .sh {
    color: #4e9a06
}

/* Literal.String.Heredoc */
.highlight .si {
    color: #4e9a06
}

/* Literal.String.Interpol */
.highlight .sx {
    color: #4e9a06
}

/* Literal.String.Other */
.highlight .sr {
    color: #4e9a06
}

/* Literal.String.Regex */
.highlight .s1 {
    color: #4e9a06
}

/* Literal.String.Single */
.highlight .ss {
    color: #4e9a06
}

/* Literal.String.Symbol */
.highlight .bp {
    color: #3465a4
}

/* Name.Builtin.Pseudo */
.highlight .fm {
    color: #000000
}

/* Name.Function.Magic */
.highlight .vc {
    color: #000000
}

/* Name.Variable.Class */
.highlight .vg {
    color: #000000
}

/* Name.Variable.Global */
.highlight .vi {
    color: #000000
}

/* Name.Variable.Instance */
.highlight .vm {
    color: #000000
}

/* Name.Variable.Magic */
.highlight .il {
    color: #0000cf;
    font-weight: bold
}

/* Literal.Number.Integer.Long */
@media not print {
    body[data-theme="dark"] .highlight pre {
        line-height: 125%;
    }

    body[data-theme="dark"] .highlight td.linenos .normal {
        color: #aaaaaa;
        background-color: transparent;
        padding-left: 5px;
        padding-right: 5px;
    }

    body[data-theme="dark"] .highlight span.linenos {
        color: #aaaaaa;
        background-color: transparent;
        padding-left: 5px;
        padding-right: 5px;
    }

    body[data-theme="dark"] .highlight td.linenos .special {
        color: #000000;
        background-color: #ffffc0;
        padding-left: 5px;
        padding-right: 5px;
    }

    body[data-theme="dark"] .highlight span.linenos.special {
        color: #000000;
        background-color: #ffffc0;
        padding-left: 5px;
        padding-right: 5px;
    }

    body[data-theme="dark"] .highlight .hll {
        background-color: #404040
    }

    body[data-theme="dark"] .highlight {
        background: #202020;
        color: #d0d0d0
    }

    body[data-theme="dark"] .highlight .c {
        color: #ababab;
        font-style: italic
    }

    /* Comment */
    body[data-theme="dark"] .highlight .err {
        color: #a61717;
        background-color: #e3d2d2
    }

    /* Error */
    body[data-theme="dark"] .highlight .esc {
        color: #d0d0d0
    }

    /* Escape */
    body[data-theme="dark"] .highlight .g {
        color: #d0d0d0
    }

    /* Generic */
    body[data-theme="dark"] .highlight .k {
        color: #6ebf26;
        font-weight: bold
    }

    /* Keyword */
    body[data-theme="dark"] .highlight .l {
        color: #d0d0d0
    }

    /* Literal */
    body[data-theme="dark"] .highlight .n {
        color: #d0d0d0
    }

    /* Name */
    body[data-theme="dark"] .highlight .o {
        color: #d0d0d0
    }

    /* Operator */
    body[data-theme="dark"] .highlight .x {
        color: #d0d0d0
    }

    /* Other */
    body[data-theme="dark"] .highlight .p {
        color: #d0d0d0
    }

    /* Punctuation */
    body[data-theme="dark"] .highlight .ch {
        color: #ababab;
        font-style: italic
    }

    /* Comment.Hashbang */
    body[data-theme="dark"] .highlight .cm {
        color: #ababab;
        font-style: italic
    }

    /* Comment.Multiline */
    body[data-theme="dark"] .highlight .cp {
        color: #cd2828;
        font-weight: bold
    }

    /* Comment.Preproc */
    body[data-theme="dark"] .highlight .cpf {
        color: #ababab;
        font-style: italic
    }

    /* Comment.PreprocFile */
    body[data-theme="dark"] .highlight .c1 {
        color: #ababab;
        font-style: italic
    }

    /* Comment.Single */
    body[data-theme="dark"] .highlight .cs {
        color: #e50808;
        font-weight: bold;
        background-color: #520000
    }

    /* Comment.Special */
    body[data-theme="dark"] .highlight .gd {
        color: #d22323
    }

    /* Generic.Deleted */
    body[data-theme="dark"] .highlight .ge {
        color: #d0d0d0;
        font-style: italic
    }

    /* Generic.Emph */
    body[data-theme="dark"] .highlight .gr {
        color: #d22323
    }

    /* Generic.Error */
    body[data-theme="dark"] .highlight .gh {
        color: #ffffff;
        font-weight: bold
    }

    /* Generic.Heading */
    body[data-theme="dark"] .highlight .gi {
        color: #589819
    }

    /* Generic.Inserted */
    body[data-theme="dark"] .highlight .go {
        color: #cccccc
    }

    /* Generic.Output */
    body[data-theme="dark"] .highlight .gp {
        color: #aaaaaa
    }

    /* Generic.Prompt */
    body[data-theme="dark"] .highlight .gs {
        color: #d0d0d0;
        font-weight: bold
    }

    /* Generic.Strong */
    body[data-theme="dark"] .highlight .gu {
        color: #ffffff;
        text-decoration: underline
    }

    /* Generic.Subheading */
    body[data-theme="dark"] .highlight .gt {
        color: #d22323
    }

    /* Generic.Traceback */
    body[data-theme="dark"] .highlight .kc {
        color: #6ebf26;
        font-weight: bold
    }

    /* Keyword.Constant */
    body[data-theme="dark"] .highlight .kd {
        color: #6ebf26;
        font-weight: bold
    }

    /* Keyword.Declaration */
    body[data-theme="dark"] .highlight .kn {
        color: #6ebf26;
        font-weight: bold
    }

    /* Keyword.Namespace */
    body[data-theme="dark"] .highlight .kp {
        color: #6ebf26
    }

    /* Keyword.Pseudo */
    body[data-theme="dark"] .highlight .kr {
        color: #6ebf26;
        font-weight: bold
    }

    /* Keyword.Reserved */
    body[data-theme="dark"] .highlight .kt {
        color: #6ebf26;
        font-weight: bold
    }

    /* Keyword.Type */
    body[data-theme="dark"] .highlight .ld {
        color: #d0d0d0
    }

    /* Literal.Date */
    body[data-theme="dark"] .highlight .m {
        color: #51b2fd
    }

    /* Literal.Number */
    body[data-theme="dark"] .highlight .s {
        color: #ed9d13
    }

    /* Literal.String */
    body[data-theme="dark"] .highlight .na {
        color: #bbbbbb
    }

    /* Name.Attribute */
    body[data-theme="dark"] .highlight .nb {
        color: #2fbccd
    }

    /* Name.Builtin */
    body[data-theme="dark"] .highlight .nc {
        color: #71adff;
        text-decoration: underline
    }

    /* Name.Class */
    body[data-theme="dark"] .highlight .no {
        color: #40ffff
    }

    /* Name.Constant */
    body[data-theme="dark"] .highlight .nd {
        color: #ffa500
    }

    /* Name.Decorator */
    body[data-theme="dark"] .highlight .ni {
        color: #d0d0d0
    }

    /* Name.Entity */
    body[data-theme="dark"] .highlight .ne {
        color: #bbbbbb
    }

    /* Name.Exception */
    body[data-theme="dark"] .highlight .nf {
        color: #71adff
    }

    /* Name.Function */
    body[data-theme="dark"] .highlight .nl {
        color: #d0d0d0
    }

    /* Name.Label */
    body[data-theme="dark"] .highlight .nn {
        color: #71adff;
        text-decoration: underline
    }

    /* Name.Namespace */
    body[data-theme="dark"] .highlight .nx {
        color: #d0d0d0
    }

    /* Name.Other */
    body[data-theme="dark"] .highlight .py {
        color: #d0d0d0
    }

    /* Name.Property */
    body[data-theme="dark"] .highlight .nt {
        color: #6ebf26;
        font-weight: bold
    }

    /* Name.Tag */
    body[data-theme="dark"] .highlight .nv {
        color: #40ffff
    }

    /* Name.Variable */
    body[data-theme="dark"] .highlight .ow {
        color: #6ebf26;
        font-weight: bold
    }

    /* Operator.Word */
    body[data-theme="dark"] .highlight .pm {
        color: #d0d0d0
    }

    /* Punctuation.Marker */
    body[data-theme="dark"] .highlight .w {
        color: #666666
    }

    /* Text.Whitespace */
    body[data-theme="dark"] .highlight .mb {
        color: #51b2fd
    }

    /* Literal.Number.Bin */
    body[data-theme="dark"] .highlight .mf {
        color: #51b2fd
    }

    /* Literal.Number.Float */
    body[data-theme="dark"] .highlight .mh {
        color: #51b2fd
    }

    /* Literal.Number.Hex */
    body[data-theme="dark"] .highlight .mi {
        color: #51b2fd
    }

    /* Literal.Number.Integer */
    body[data-theme="dark"] .highlight .mo {
        color: #51b2fd
    }

    /* Literal.Number.Oct */
    body[data-theme="dark"] .highlight .sa {
        color: #ed9d13
    }

    /* Literal.String.Affix */
    body[data-theme="dark"] .highlight .sb {
        color: #ed9d13
    }

    /* Literal.String.Backtick */
    body[data-theme="dark"] .highlight .sc {
        color: #ed9d13
    }

    /* Literal.String.Char */
    body[data-theme="dark"] .highlight .dl {
        color: #ed9d13
    }

    /* Literal.String.Delimiter */
    body[data-theme="dark"] .highlight .sd {
        color: #ed9d13
    }

    /* Literal.String.Doc */
    body[data-theme="dark"] .highlight .s2 {
        color: #ed9d13
    }

    /* Literal.String.Double */
    body[data-theme="dark"] .highlight .se {
        color: #ed9d13
    }

    /* Literal.String.Escape */
    body[data-theme="dark"] .highlight .sh {
        color: #ed9d13
    }

    /* Literal.String.Heredoc */
    body[data-theme="dark"] .highlight .si {
        color: #ed9d13
    }

    /* Literal.String.Interpol */
    body[data-theme="dark"] .highlight .sx {
        color: #ffa500
    }

    /* Literal.String.Other */
    body[data-theme="dark"] .highlight .sr {
        color: #ed9d13
    }

    /* Literal.String.Regex */
    body[data-theme="dark"] .highlight .s1 {
        color: #ed9d13
    }

    /* Literal.String.Single */
    body[data-theme="dark"] .highlight .ss {
        color: #ed9d13
    }

    /* Literal.String.Symbol */
    body[data-theme="dark"] .highlight .bp {
        color: #2fbccd
    }

    /* Name.Builtin.Pseudo */
    body[data-theme="dark"] .highlight .fm {
        color: #71adff
    }

    /* Name.Function.Magic */
    body[data-theme="dark"] .highlight .vc {
        color: #40ffff
    }

    /* Name.Variable.Class */
    body[data-theme="dark"] .highlight .vg {
        color: #40ffff
    }

    /* Name.Variable.Global */
    body[data-theme="dark"] .highlight .vi {
        color: #40ffff
    }

    /* Name.Variable.Instance */
    body[data-theme="dark"] .highlight .vm {
        color: #40ffff
    }

    /* Name.Variable.Magic */
    body[data-theme="dark"] .highlight .il {
        color: #51b2fd
    }

    /* Literal.Number.Integer.Long */
    @media (prefers-color-scheme: dark) {
        body:not([data-theme="light"]) .highlight pre {
            line-height: 125%;
        }

        body:not([data-theme="light"]) .highlight td.linenos .normal {
            color: #aaaaaa;
            background-color: transparent;
            padding-left: 5px;
            padding-right: 5px;
        }

        body:not([data-theme="light"]) .highlight span.linenos {
            color: #aaaaaa;
            background-color: transparent;
            padding-left: 5px;
            padding-right: 5px;
        }

        body:not([data-theme="light"]) .highlight td.linenos .special {
            color: #000000;
            background-color: #ffffc0;
            padding-left: 5px;
            padding-right: 5px;
        }

        body:not([data-theme="light"]) .highlight span.linenos.special {
            color: #000000;
            background-color: #ffffc0;
            padding-left: 5px;
            padding-right: 5px;
        }

        body:not([data-theme="light"]) .highlight .hll {
            background-color: #404040
        }

        body:not([data-theme="light"]) .highlight {
            background: #202020;
            color: #d0d0d0
        }

        body:not([data-theme="light"]) .highlight .c {
            color: #ababab;
            font-style: italic
        }

        /* Comment */
        body:not([data-theme="light"]) .highlight .err {
            color: #a61717;
            background-color: #e3d2d2
        }

        /* Error */
        body:not([data-theme="light"]) .highlight .esc {
            color: #d0d0d0
        }

        /* Escape */
        body:not([data-theme="light"]) .highlight .g {
            color: #d0d0d0
        }

        /* Generic */
        body:not([data-theme="light"]) .highlight .k {
            color: #6ebf26;
            font-weight: bold
        }

        /* Keyword */
        body:not([data-theme="light"]) .highlight .l {
            color: #d0d0d0
        }

        /* Literal */
        body:not([data-theme="light"]) .highlight .n {
            color: #d0d0d0
        }

        /* Name */
        body:not([data-theme="light"]) .highlight .o {
            color: #d0d0d0
        }

        /* Operator */
        body:not([data-theme="light"]) .highlight .x {
            color: #d0d0d0
        }

        /* Other */
        body:not([data-theme="light"]) .highlight .p {
            color: #d0d0d0
        }

        /* Punctuation */
        body:not([data-theme="light"]) .highlight .ch {
            color: #ababab;
            font-style: italic
        }

        /* Comment.Hashbang */
        body:not([data-theme="light"]) .highlight .cm {
            color: #ababab;
            font-style: italic
        }

        /* Comment.Multiline */
        body:not([data-theme="light"]) .highlight .cp {
            color: #cd2828;
            font-weight: bold
        }

        /* Comment.Preproc */
        body:not([data-theme="light"]) .highlight .cpf {
            color: #ababab;
            font-style: italic
        }

        /* Comment.PreprocFile */
        body:not([data-theme="light"]) .highlight .c1 {
            color: #ababab;
            font-style: italic
        }

        /* Comment.Single */
        body:not([data-theme="light"]) .highlight .cs {
            color: #e50808;
            font-weight: bold;
            background-color: #520000
        }

        /* Comment.Special */
        body:not([data-theme="light"]) .highlight .gd {
            color: #d22323
        }

        /* Generic.Deleted */
        body:not([data-theme="light"]) .highlight .ge {
            color: #d0d0d0;
            font-style: italic
        }

        /* Generic.Emph */
        body:not([data-theme="light"]) .highlight .gr {
            color: #d22323
        }

        /* Generic.Error */
        body:not([data-theme="light"]) .highlight .gh {
            color: #ffffff;
            font-weight: bold
        }

        /* Generic.Heading */
        body:not([data-theme="light"]) .highlight .gi {
            color: #589819
        }

        /* Generic.Inserted */
        body:not([data-theme="light"]) .highlight .go {
            color: #cccccc
        }

        /* Generic.Output */
        body:not([data-theme="light"]) .highlight .gp {
            color: #aaaaaa
        }

        /* Generic.Prompt */
        body:not([data-theme="light"]) .highlight .gs {
            color: #d0d0d0;
            font-weight: bold
        }

        /* Generic.Strong */
        body:not([data-theme="light"]) .highlight .gu {
            color: #ffffff;
            text-decoration: underline
        }

        /* Generic.Subheading */
        body:not([data-theme="light"]) .highlight .gt {
            color: #d22323
        }

        /* Generic.Traceback */
        body:not([data-theme="light"]) .highlight .kc {
            color: #6ebf26;
            font-weight: bold
        }

        /* Keyword.Constant */
        body:not([data-theme="light"]) .highlight .kd {
            color: #6ebf26;
            font-weight: bold
        }

        /* Keyword.Declaration */
        body:not([data-theme="light"]) .highlight .kn {
            color: #6ebf26;
            font-weight: bold
        }

        /* Keyword.Namespace */
        body:not([data-theme="light"]) .highlight .kp {
            color: #6ebf26
        }

        /* Keyword.Pseudo */
        body:not([data-theme="light"]) .highlight .kr {
            color: #6ebf26;
            font-weight: bold
        }

        /* Keyword.Reserved */
        body:not([data-theme="light"]) .highlight .kt {
            color: #6ebf26;
            font-weight: bold
        }

        /* Keyword.Type */
        body:not([data-theme="light"]) .highlight .ld {
            color: #d0d0d0
        }

        /* Literal.Date */
        body:not([data-theme="light"]) .highlight .m {
            color: #51b2fd
        }

        /* Literal.Number */
        body:not([data-theme="light"]) .highlight .s {
            color: #ed9d13
        }

        /* Literal.String */
        body:not([data-theme="light"]) .highlight .na {
            color: #bbbbbb
        }

        /* Name.Attribute */
        body:not([data-theme="light"]) .highlight .nb {
            color: #2fbccd
        }

        /* Name.Builtin */
        body:not([data-theme="light"]) .highlight .nc {
            color: #71adff;
            text-decoration: underline
        }

        /* Name.Class */
        body:not([data-theme="light"]) .highlight .no {
            color: #40ffff
        }

        /* Name.Constant */
        body:not([data-theme="light"]) .highlight .nd {
            color: #ffa500
        }

        /* Name.Decorator */
        body:not([data-theme="light"]) .highlight .ni {
            color: #d0d0d0
        }

        /* Name.Entity */
        body:not([data-theme="light"]) .highlight .ne {
            color: #bbbbbb
        }

        /* Name.Exception */
        body:not([data-theme="light"]) .highlight .nf {
            color: #71adff
        }

        /* Name.Function */
        body:not([data-theme="light"]) .highlight .nl {
            color: #d0d0d0
        }

        /* Name.Label */
        body:not([data-theme="light"]) .highlight .nn {
            color: #71adff;
            text-decoration: underline
        }

        /* Name.Namespace */
        body:not([data-theme="light"]) .highlight .nx {
            color: #d0d0d0
        }

        /* Name.Other */
        body:not([data-theme="light"]) .highlight .py {
            color: #d0d0d0
        }

        /* Name.Property */
        body:not([data-theme="light"]) .highlight .nt {
            color: #6ebf26;
            font-weight: bold
        }

        /* Name.Tag */
        body:not([data-theme="light"]) .highlight .nv {
            color: #40ffff
        }

        /* Name.Variable */
        body:not([data-theme="light"]) .highlight .ow {
            color: #6ebf26;
            font-weight: bold
        }

        /* Operator.Word */
        body:not([data-theme="light"]) .highlight .pm {
            color: #d0d0d0
        }

        /* Punctuation.Marker */
        body:not([data-theme="light"]) .highlight .w {
            color: #666666
        }

        /* Text.Whitespace */
        body:not([data-theme="light"]) .highlight .mb {
            color: #51b2fd
        }

        /* Literal.Number.Bin */
        body:not([data-theme="light"]) .highlight .mf {
            color: #51b2fd
        }

        /* Literal.Number.Float */
        body:not([data-theme="light"]) .highlight .mh {
            color: #51b2fd
        }

        /* Literal.Number.Hex */
        body:not([data-theme="light"]) .highlight .mi {
            color: #51b2fd
        }

        /* Literal.Number.Integer */
        body:not([data-theme="light"]) .highlight .mo {
            color: #51b2fd
        }

        /* Literal.Number.Oct */
        body:not([data-theme="light"]) .highlight .sa {
            color: #ed9d13
        }

        /* Literal.String.Affix */
        body:not([data-theme="light"]) .highlight .sb {
            color: #ed9d13
        }

        /* Literal.String.Backtick */
        body:not([data-theme="light"]) .highlight .sc {
            color: #ed9d13
        }

        /* Literal.String.Char */
        body:not([data-theme="light"]) .highlight .dl {
            color: #ed9d13
        }

        /* Literal.String.Delimiter */
        body:not([data-theme="light"]) .highlight .sd {
            color: #ed9d13
        }

        /* Literal.String.Doc */
        body:not([data-theme="light"]) .highlight .s2 {
            color: #ed9d13
        }

        /* Literal.String.Double */
        body:not([data-theme="light"]) .highlight .se {
            color: #ed9d13
        }

        /* Literal.String.Escape */
        body:not([data-theme="light"]) .highlight .sh {
            color: #ed9d13
        }

        /* Literal.String.Heredoc */
        body:not([data-theme="light"]) .highlight .si {
            color: #ed9d13
        }

        /* Literal.String.Interpol */
        body:not([data-theme="light"]) .highlight .sx {
            color: #ffa500
        }

        /* Literal.String.Other */
        body:not([data-theme="light"]) .highlight .sr {
            color: #ed9d13
        }

        /* Literal.String.Regex */
        body:not([data-theme="light"]) .highlight .s1 {
            color: #ed9d13
        }

        /* Literal.String.Single */
        body:not([data-theme="light"]) .highlight .ss {
            color: #ed9d13
        }

        /* Literal.String.Symbol */
        body:not([data-theme="light"]) .highlight .bp {
            color: #2fbccd
        }

        /* Name.Builtin.Pseudo */
        body:not([data-theme="light"]) .highlight .fm {
            color: #71adff
        }

        /* Name.Function.Magic */
        body:not([data-theme="light"]) .highlight .vc {
            color: #40ffff
        }

        /* Name.Variable.Class */
        body:not([data-theme="light"]) .highlight .vg {
            color: #40ffff
        }

        /* Name.Variable.Global */
        body:not([data-theme="light"]) .highlight .vi {
            color: #40ffff
        }

        /* Name.Variable.Instance */
        body:not([data-theme="light"]) .highlight .vm {
            color: #40ffff
        }

        /* Name.Variable.Magic */
        body:not([data-theme="light"]) .highlight .il {
            color: #51b2fd
        }

        /* Literal.Number.Integer.Long */
    }
}
