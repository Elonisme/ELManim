from manim import *
from matplotlib.pyplot import gray
from nbformat import write
import werkzeug


class Middle(Scene):
    def construct(self):
        # self.add_sound(r"Vincent Rubinetti - The Music of 3Blue1Brown\Vincent Rubinetti - The Music of 3Blue1Brown - 01 Zeta.mp3")
        section1 = Tex("项目介绍", tex_template=TexTemplateLibrary.ctex, font_size=30, color=RED_E)
        self.play(Write(section1))
        self.wait()
        self.play(
            FadeOut(section1)
            )

        algorithm = Tex(r"算法\\TOPSIS综合评价法\\熵权法\\灰色预测\\BP神经网络预测", tex_template=TexTemplateLibrary.ctex, font_size=30)
        language= Tex(r"采用语言MatLab进行编程", tex_template=TexTemplateLibrary.ctex, font_size=30).move_to(algorithm).shift(DOWN*1.2)
        AL = VGroup(algorithm,language).shift(UP*0.5)
        self.play(Write(AL))
        self.wait(2)
        self.play(FadeOut(AL))
  

        section2 = Tex("TOPSIS综合评价法", tex_template=TexTemplateLibrary.ctex, font_size=30, color=RED_E)
        self.play(Write(section2))
        self.wait()
        self.play(
            FadeOut(section2),
            )
        section2.font_size=20
        section2.to_edge(LEFT+UP*2.5)
        self.play(FadeIn(section2))
        TOPSIS = Tex(r"OPSIS法是用来处理指标决策问题的多方案排序和选择的方法,它的基本思想是:依据理想点的理论原理，\\找寻距离理想点最近的方案。并通过计算对象与最优解、最劣解的距离大小，确定顺序。即先设定一个\\ 虚拟的最优解（又称正理想解)和一个最劣解（又称负理想解)，将各备选方案与正负理想解相互比较，\\若方案最靠近最优解即又距最劣解最远, 为最好。TOPSIS方法需要的评价指标决策矩阵和指标权重,\\本项目由熵权法计算给出", tex_template=TexTemplateLibrary.ctex, font_size=20)
        
        TOPSISTex1 = Tex(r"每个环境指标的最大值，记为 ，组成向量:", tex_template=TexTemplateLibrary.ctex, font_size=25, color=RED_E).shift(UP)
        TOPSISMath1 = MathTex(r"z^+ ={z_ {1}^{+},  z_ {2}^ {+},\cdots,z_ {m}^ {+}}", font_size=20).move_to(TOPSISTex1).shift(DOWN)
        TOPSISTex2 =  Tex(r"该向量代表了环境最好的年份。同样的，找出每列也就是每个指标的最小值，记为,组成向量: 该向量代表了环境最差的年份.", tex_template=TexTemplateLibrary.ctex, font_size=20).move_to(TOPSISMath1).shift(DOWN)
        TOPSISMath2 = MathTex(r"z^- ={z_ {1}^{-},  z_ {2}^ {-},\cdots,z_ {m}^ {-}}", font_size=20).move_to(TOPSISTex2).shift(DOWN)


        TOPSISTex3 =  Tex(r"定义第i个年份与理想目标距离为 ，计算公式为", tex_template=TexTemplateLibrary.ctex, font_size=25, color=RED_E).shift(UP)
        TOPSISMath3 = MathTex(r"D_i^+=\sqrt{\sum_{j=1}^{m}{w_j(z_j^+-z_{ij})^2}}", font_size=20).move_to(TOPSISTex3).shift(DOWN)
        TOPSISTex4 =  Tex(r"定义第i个年份与不理想目标距离为 ，计算公式为", tex_template=TexTemplateLibrary.ctex, font_size=25, color=RED_E).move_to(TOPSISMath3).shift(DOWN)
        TOPSISMath4 = MathTex(r"D_i^-=\sqrt{\sum_{j=1}^{m}{w_j(z_j^--z_{ij})^2}}", font_size=20).move_to(TOPSISTex4).shift(DOWN)

        TOPSISTex5 =  Tex(r"定义第i个年份的得分为 ，计算公式为", tex_template=TexTemplateLibrary.ctex, font_size=25, color=RED_E).shift(UP)
        TOPSISMath5 = MathTex(r"S_i=\frac{D_i^-}{D_i^++D_i^-}", font_size=20).move_to(TOPSISTex5).shift(DOWN)
        TOPSISTex6 = Tex(r" 当Si越接近于1，说明此年份i距离理想化目标越近,该年份环境就越好。反之，当 越接近于0，说明年份i距离理想化目标越远,该年份环境就越差.", tex_template=TexTemplateLibrary.ctex, font_size=20).move_to(TOPSISMath5).shift(DOWN)

        MathGruop1 = VGroup(
            TOPSISTex1,
            TOPSISMath1,
            TOPSISTex2,
            TOPSISMath2,
            )

        MathGruop2 = VGroup(
            TOPSISTex3,
            TOPSISMath3,
            TOPSISTex4,
            TOPSISMath4,
        )

        MathGruop3 = VGroup(
            TOPSISTex5,
            TOPSISMath5,
            TOPSISTex6
        )
        self.play(
            Write(TOPSIS)
            )
        self.wait(2)
        self.play(
            FadeOut(TOPSIS)
            )

        self.play(
            Write(MathGruop1),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop1))

        self.play(
            Write(MathGruop2),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop2))

        self.play(
            Write(MathGruop3),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop3))


        self.play(Unwrite(section2))

        section3 = Tex("熵权法", tex_template=TexTemplateLibrary.ctex, font_size=30, color=RED_E)
        self.play(Write(section3))
        self.wait()
        self.play(
            FadeOut(section3)
            )
        section3.font_size=20
        section3.to_edge(LEFT+UP*2.5)

        self.play(FadeIn(section3))
        Entropy = Tex(r"熵权法是一个客观的赋权方法,可以最大程度上避免主观性赋权对于环境指标量化结果的影响。熵权法权法依据的原理是指标的变异程度，即变异程度越高则对应的权值也就越高。", tex_template=TexTemplateLibrary.ctex, font_size=25)
        EntropyTex1 = Tex(r"首先需要对环境指标数据进行正向化和归一化处理\\其中$z_{ij}$为归一化处理后的变量, $x_{min}$和$x_{max}$分别为每个指标的最大值和最值", tex_template=TexTemplateLibrary.ctex, font_size=25).shift(UP)
        EntropyMath1 = MathTex(r"z_{ij}=\frac{x_{ij}-x_{min}}{x_{max}-x_{min}}", font_size=20).move_to(EntropyTex1).shift(DOWN)

        EntropyTex2 = Tex(r"第j个环境指标下第i个年份所占权重，将其看作计算信息熵时的概率$p_{ij}$", tex_template=TexTemplateLibrary.ctex, font_size=25).shift(UP)
        EntropyMath2 = MathTex(r"p_{ij}=\frac{z_{ij}}{\sum_{i=1}^{n}z_{ij}}", font_size=20).move_to(EntropyTex2).shift(DOWN)

        EntropyTex3 = Tex(r"计算第j个环境指标的信息熵$e_j$ ，并计算对应信息效用值$d_j$ ", tex_template=TexTemplateLibrary.ctex, font_size=25).shift(UP)
        EntropyMath3 = MathTex(r"e_j=-\frac{1}{ln{n}}\sum_{i=1}^{n}{ln{(}p_{ij})}", font_size=20).move_to(EntropyTex3).shift(DOWN)
        EntropyTex4 = Tex(r"此处进行转换的原因是因为信息熵越大代表该环境指标的信息越少，引入$d_j$就可以正向衡量信息量。", tex_template=TexTemplateLibrary.ctex, font_size=25).move_to(EntropyMath3).shift(DOWN)
        EntropyMath4 = MathTex(r"d_j=1-e_j", font_size=20).move_to(EntropyTex4).shift(DOWN)

        EntropyTex5 = Tex(r"最终归一化得到每个环境评价指标的熵权$w_j$", tex_template=TexTemplateLibrary.ctex, font_size=25).shift(UP)
        EntropyMath5 = MathTex(r"w_j=\frac{d_j}{\sum_{j=1}^{m}d_j}", font_size=20).move_to(EntropyTex5).shift(DOWN)

        MathGruop4 = VGroup(
            EntropyTex1,
            EntropyMath1
        )
        MathGruop5 = VGroup(
            EntropyTex2,
            EntropyMath2
        )
        MathGruop6 = VGroup(
            EntropyTex3,
            EntropyMath3,
            EntropyTex4,
            EntropyMath4
        )
        # MathGruop7 = VGroup(
        #     EntropyTex5,
        #     EntropyMath5
        # )
        self.play(Write(Entropy),run_time = 2)
        self.wait(2)
        self.play(Unwrite(Entropy))

        self.play(
            Write(MathGruop4),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop4))
        
        self.play(
            Write(MathGruop5),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop5))

        self.play(
            Write(MathGruop6),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(MathGruop6))

        self.play(
            Write(EntropyTex5),
            Write(EntropyMath5),
            run_time = 2
        )
        self.wait(2)
        self.play(
            FadeOut(EntropyTex5),
            FadeOut(EntropyMath5)
            )

        self.play(Unwrite(section3))

        section4 = Tex("灰色预测", tex_template=TexTemplateLibrary.ctex, font_size=30, color=RED_E)
        self.play(Write(section4))
        self.wait()
        self.play(
            FadeOut(section4)
            )
        section4.font_size=20
        section4.to_edge(LEFT+UP*2.5)
        self.play(Write(section4))
        

        AQI = Tex(r"空气质量指数（Air Quality Index，简称AQI），是一个用来定量描述空气质量水平的数值。AQI的取值范围位于0-500 之间。环境空气污染物的种类有很多，参与AQI指数评价的有二氧化硫(SO2)、二氧化氮(NO2)、一氧化碳(CO)、臭氧(O3)、PM2.5、PM10。", tex_template=TexTemplateLibrary.ctex, font_size=25)
        self.play(Write(AQI))
        self.play(Unwrite(AQI))
        AQI2 = Tex(r"空气质量指数的值在不同的区间，就代表了不同的空气质量水平。比如0-50之间，代表良好；51-100之间，代表中等；101-150之间代表轻度污染等等。为了更直观起见，每个区间都有一个固定的颜色值与它对应：", tex_template=TexTemplateLibrary.ctex, font_size=25).shift(UP)
        AQIimg = ImageMobject(r"AQItable.png").move_to(AQI2).shift(DOWN*2)
        # AQIGruop1 = VGroup(
        #     AQI2,
        #     AQIimg
        # )
        self.play(
            Write(AQI2),
            FadeIn(AQIimg)
            )
            
        self.wait(2)
        self.play(
            Unwrite(AQI2),
            FadeOut(AQIimg)
            )
        AQI25 = Tex(r"AQI的折算公式如下：", tex_template=TexTemplateLibrary.ctex, font_size=25).shift(UP)
        AQIMath = MathTex(r"I=\frac{I_{high}-I_{low}}{C_{high}-C_{low}}(C-C_{low})+I_{low})", font_size=20).move_to(AQI25).shift(DOWN)
        AQI3 = Tex(r"其中I等于空气质量指数，即AQI，输出值；C为污染物浓度，输入值； $C_{low}$为小于或等于C的浓度限值； $C_{high}$为大于或等于C的浓度限值； $I_{low}$对应于$C_{low}$的指数限值；$I_{high}$为对应于$C_{high}$的指数限值。", tex_template=TexTemplateLibrary.ctex, font_size=25).move_to(AQIMath).shift(DOWN)
        AQIGruop2 = VGroup(
            AQI25,
            AQIMath,
            AQI3
        )
        self.play(Write(AQIGruop2))
        self.wait(2)
        self.play(Unwrite(AQIGruop2))
        gray = Tex(r"一次累加生成序列：", tex_template=TexTemplateLibrary.ctex, font_size=25).shift(UP)
        GrayMath = MathTex("x^{(0)}=(x^{(0)}(1),x^{(0)}(2),...,x^{(0)}(10))", font_size=20).move_to(gray).shift(DOWN)
        AQIGruop3 = VGroup(
            gray,
            GrayMath
        )
        self.play(Write(AQIGruop3))
        self.wait(2)
        self.play(Unwrite(AQIGruop3))
        gray2 = Tex(r"$x^{(1)}$的均值生成序列", tex_template=TexTemplateLibrary.ctex, font_size=25).shift(UP)
        GrayMath2 = MathTex("z^{(1)}=(z^{(1)}(2),z^{(1)}(3),...,z^{(1)}(n))", font_size=20).move_to(gray2).shift(DOWN)
        AQIGruop4 = VGroup(
            gray2,
            GrayMath2
        )
        self.play(Write(AQIGruop4))
        self.wait()
        self.play(Unwrite(AQIGruop4))
        Garymin = Tex(r"建立灰微分方程", tex_template=TexTemplateLibrary.ctex, font_size=25).shift(UP*2)
        GarymimMath = MathTex("x^{(0)}(k)+az^{(1)}(k)=b,k=2,3,...,10", font_size=20).move_to(Garymin).shift(DOWN)
        Whitemin = Tex(r"建立白微分方程", tex_template=TexTemplateLibrary.ctex, font_size=25).move_to(GarymimMath).shift(DOWN)
        WhiteminMath = MathTex(r"\frac{dx^{(1)}}{dt}+ax^{(1)}(t)=b", font_size=20).move_to(Whitemin).shift(DOWN)
        AQIGruop5 = VGroup(
            Garymin,
            GarymimMath,
            Whitemin,
            WhiteminMath
        )
        self.play(Write(AQIGruop5))
        self.wait()
        self.play(Unwrite(AQIGruop5))
        
        GRAYMath3 = Tex(r"于是得到方程：", tex_template=TexTemplateLibrary.ctex, font_size=25).shift(UP)
        GRAYMath3Model = MathTex(r"\hat{x}(k+1)=(x^{(0)}(1)-\frac{\hat{b}}{\hat{a}})e^{-\hat{a}k}+\frac{\hat{b}}{\hat{a}},k=0,1,...,10", font_size=20).move_to(GRAYMath3).shift(DOWN)
        AQIGruop6 = VGroup(
            GRAYMath3,
            GRAYMath3Model
        )
        self.play(Write(AQIGruop6))
        self.wait()
        self.play(Unwrite(AQIGruop6))
        GaryResult = Tex(r"计算得到发展系数$a_1=\mathrm{0.0119639}$ 灰色作用量$b_1=\mathrm{95.7210532}$ ", tex_template=TexTemplateLibrary.ctex, font_size=25)
        self.play(Write(GaryResult))
        self.wait()
        self.play(Unwrite(GaryResult))

        self.play(Unwrite(section4))
        

        SceneFileWriter.get_resolution_directory(r"media\videos\NetWorks\2160p60\mynetwork.mp4")

        section5 = Tex("BP神经网络预测", tex_template=TexTemplateLibrary.ctex, font_size=30, color=RED_E)
        self.play(Write(section5))
        self.wait()
        self.play(
            FadeOut(section5)
            )
        section5.font_size=20
        section5.to_edge(LEFT+UP*2.5)
        self.play(FadeIn(section5))
       
        self.play(Unwrite(section5))

        section6 = Tex("软件安装与卸载", tex_template=TexTemplateLibrary.ctex, font_size=30, color=RED_E)
        self.play(Write(section6))
        self.wait()
        self.play(Unwrite(section6))
        self.wait()