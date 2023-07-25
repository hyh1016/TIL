# Tiles

## 정의

반복적으로 사용되는 레이아웃(header, footer 등) 정보를 재사용할 수 있도록 페이지 구성을 관리하는 프레임워크

단순히 파일을 합쳐주는 JSP Include와 달리, ajax처럼 부분적 재렌더링이 가능하다.

## 3요소

### Template

* 페이지 레이아웃
* jsp로 페이지의 기본 골격만 구성하고 각 페이지의 실제 내용은 definition에서 설정되는 Attribute 태그를 사용하여 런타임에 뿌림

### Attribute

* Template의 빈 공간을 채우기 위해 사용되는 정보
* 3가지 타입으로 구성
  * template
  * definition
  * string

### Definition

* 사용자에게 제공하기 위해 렌더링되는 Template과 Attribute 연결

## 사용법

1.  **`pom.xml` 에 tiles를 사용하기 위한 모듈 dependency 추가**

    ```java
    <dependency> 
     	<groupId>org.apache.tiles</groupId> 
        <artifactId>tiles-jsp</artifactId> 
        <version>버전</version> 
     </dependency>
     <dependency> 
       <groupId>org.apache.tiles</groupId> 
       <artifactId>tiles-template</artifactId> 
       <version>버전</version> 
     </dependency> 
    ```
2.  **`applicaitonContext.xml` 에서 탐색 우선 순위를 tiles - jsp 순으로 설정**

    ```java
    <!-- Tiles ViewResolver --> 
    <bean id="tilesViewResolver" class="org.springframework.web.servlet.view.UrlBasedViewResolver">
      <property name="viewClass" value="org.springframework.web.servlet.view.tiles2.TilesView"/> 
      <property name="order" value="1"/> //우선순위 1 - 타일즈 설정 
    </bean> 

    <!-- JSP ViewResolver --> 
    <bean id="jspViewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver"> 
      <property name="viewClass" value="org.springframework.web.servlet.view.JstlView"/> 
      <property name="prefix" value="/WEB-INF/jsp/"/> <property name="suffix" value=".jsp"/> 
      <property name="order" value="2"/> //우선순위 2 - jsp설정 
    </bean>
    ```

    즉, tiles 파일(설정 파일에 정의된 definition과 완전히 일치하는 jsp 파일)이 있으면 이걸 먼저 선택하고, 없다면 일반적인 jsp 파일을 선택한다.
3.  **tiles 설정 파일(xml) 작성**

    ```java
    <?xml version="1.0" encoding="UTF-8" ?> 
    <!DOCTYPE tiles-definitions PUBLIC "-//Apache Software Foundation//DTD Tiles Configuration 2.1//EN" "http://tiles.apache.org/dtds/tiles-config_2_1.dtd"> 
    <tiles-definitions>
        <definition name="page1/*">
            <put-attribute name="title" value="test" /> 
            <put-attribute name="header" value="/WEB-INF/views/common/header.jsp" />
            <put-attribute name="body" value="WEB-INF/views/page1/{1}.jsp" /> 
            <put-attribute name="bottom" value="/WEB-INF/views/common/bottom.jsp" /> 
        </definition>
    </tiles-definitions>
    ```

    * 태그 안에 definition들을 정의한다.
    * `definition`에는 다음의 정보들이 포함된다.
      * 이름 (다른 definition에서 상속 등의 참조를 하기 위해)
      * 템플릿 (이 definition이 사용될 jsp 레이아웃 파일 경로)
        * 이를 생략하면
    * `definition` 내에 정의되는 `attribute`에는 다음의 정보들이 포함된다.
      * 이름 (jsp 레이아웃에서 이를 통해 attribute를 호출)
      * 값 (attribute를 호출했을 때 반환될 String/Template…)
      * `*`은 모든 문자열을 뜻함. 파일명은 `*` 디렉토리명은 `**`
      * {1}, {2}와 같은 숫자는 \*에 들어간 것을 순서대로 받음
4.  **tiles 태그를 통해 문자열, 레이아웃(jsp)를 동적으로 include**

    ```
    <**tiles:getAsString** name="title"/>
    ```

    * name이 title인 attribute의 value에 선언된 내용을 그대로 가져옴

    ```
     <**tiles:insertAttribute** name="header" />
    ```

    * name이 header인 jsp 파일의 내용을 가져옴
5.  **컨트롤러에서는 다음과 같이 매핑해서 사용**

    ```java
    @RequestMapping("/")
    public String testList (HttpServletRequest request, HttpServletResponse response, ModelMap model) {
    		return "page1/main";
    }
    ```

    * 이름이 page1/\*인 타일즈와 매핑된다.
