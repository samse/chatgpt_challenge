import styled from 'styled-components';
import React, { useState } from 'react';
import { useRecoilState, useRecoilValue, useSetRecoilState } from 'recoil';
import { DarkModeAtom } from './atoms';

const ToggleContainer = styled.div<{isOn: boolean}>`
  width: 20px;
  height: 10px;
  margin-top: 10px;
  background-color: ${props => props.isOn ? '#4cd964' : '#ccc'};
  border-radius: 5px;
  position: relative;
  transition: background-color 0.3s ease;
  cursor: pointer;
`;

const Slider = styled.div<{isOn: boolean}>`
  width: 8px;
  height: 8px;
  background-color: white;
  border-radius: 4px;
  position: absolute;
  top: 1px;
  left: ${props => props.isOn ? '11px' : '1px'};
  transition: left 0.3s ease;
`;

function CupertinoToggle() {
  const setDarkMode = useSetRecoilState(DarkModeAtom);
  const isOn = useRecoilValue(DarkModeAtom);

  const handleToggle = () => {
      setDarkMode(!isOn);
  };

  return (
    <ToggleContainer isOn={isOn} onClick={handleToggle}>
      <Slider isOn={isOn} />
    </ToggleContainer>
  );
}

export default CupertinoToggle;
