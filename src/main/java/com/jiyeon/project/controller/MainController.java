package com.jiyeon.project.controller;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
@AllArgsConstructor
public class MainController {

    @GetMapping("/docker-main")
    public ModelAndView entityManager(){

        ModelAndView mv = new ModelAndView();

        mv.setViewName("main.html");
        return mv;

    }

}
