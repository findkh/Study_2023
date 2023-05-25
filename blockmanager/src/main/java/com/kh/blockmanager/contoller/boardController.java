package com.kh.blockmanager.contoller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import lombok.RequiredArgsConstructor;

@Controller
@RequiredArgsConstructor
public class boardController {
	
	@RequestMapping(value = {"/board", "board/board.html"})
	public String board() {
		return "board";
	}

}
