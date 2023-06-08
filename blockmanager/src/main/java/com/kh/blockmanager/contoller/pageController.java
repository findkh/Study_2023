package com.kh.blockmanager.contoller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import lombok.RequiredArgsConstructor;

@Controller
@RequiredArgsConstructor
public class pageController {
	@RequestMapping(value= {"/", "/index", "/index.html"})
	public String indexMain(Model model) {
		return "index";
	}
	
	@RequestMapping(value= {"/board", "/board.html"})
	public String boardPage(Model model) {
		return "board";
	}
}
